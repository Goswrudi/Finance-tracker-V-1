"""
Fintraa — Personal Finance & Productivity Dashboard
=====================================================
PySide6 desktop UI for the Fintraa project.

This file replaces the original console prototype with a proper
sidebar-navigation dashboard, while keeping the exact same
Google / Microsoft quick-launch logic you already wrote — it's
just wired to buttons now instead of input().

Run with:  python fintraa_dashboard.py

Author: Rudransh Goswami
"""

import sys
import webbrowser
from datetime import datetime

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QFrame, QStackedWidget, QProgressBar, QScrollArea,
    QSizePolicy, QSpacerItem, QGraphicsDropShadowEffect, QLineEdit,
    QInputDialog, QTableWidget, QTableWidgetItem, QHeaderView, QButtonGroup
)


# ============================================================
#  BACKEND — same integration logic as your original script
# ============================================================

class GoogleFuncs:
    """Quick-launch handlers for Google's web-based office suite."""

    @staticmethod
    def open_sheets():
        webbrowser.open('https://sheets.google.com')

    @staticmethod
    def open_docs():
        webbrowser.open('https://docs.google.com')

    @staticmethod
    def open_slides():
        webbrowser.open('https://docs.google.com/presentation/u/0/')

    @staticmethod
    def open_calendar():
        webbrowser.open('https://calendar.google.com/')


class MicrosoftFuncs:
    """Quick-launch handlers for Microsoft's web-based office suite."""

    @staticmethod
    def open_excel():
        webbrowser.open('https://excel.cloud.microsoft/en-gb/')

    @staticmethod
    def open_word():
        webbrowser.open('https://word.cloud.microsoft/en-gb/')

    @staticmethod
    def open_powerpoint():
        webbrowser.open('https://powerpoint.cloud.microsoft/en-gb/')

    @staticmethod
    def open_365():
        webbrowser.open('https://www.microsoft.com/en-in/microsoft-365')


QUOTES = [
    "Do not save what is left after spending; spend what is left after saving.",
    "A budget is telling your money where to go instead of wondering where it went.",
    "The habit of saving is itself an education.",
    "Beware of little expenses — a small leak will sink a great ship.",
    "It's not your salary that makes you rich, it's your spending habits.",
    "Financial freedom is available to those who learn about it and work for it.",
    "Every rupee saved today is a rupee that works for you tomorrow.",
    "Do not go broke trying to look rich.",
]


def quote_of_the_day() -> str:
    """Same quote all day, rotates daily — no API needed."""
    day_index = datetime.now().timetuple().tm_yday
    return QUOTES[day_index % len(QUOTES)]


# ============================================================
#  THEME
# ============================================================

COLORS = {
    "bg": "#0F1420",
    "sidebar": "#141A29",
    "card": "#1A2233",
    "card_alt": "#1E2739",
    "border": "#252F45",
    "text": "#E7ECF5",
    "text_dim": "#8B93A7",
    "accent": "#2FE6A6",
    "accent_dim": "#1FA37A",
    "danger": "#FF6B6B",
    "warning": "#FFC24B",
}

STYLE_SHEET = f"""
QWidget {{
    background-color: {COLORS['bg']};
    color: {COLORS['text']};
    font-family: "Segoe UI", "Inter", sans-serif;
}}

QScrollArea {{
    border: none;
}}

QScrollBar:vertical {{
    background: transparent;
    width: 8px;
    margin: 0;
}}
QScrollBar::handle:vertical {{
    background: {COLORS['border']};
    border-radius: 4px;
    min-height: 30px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QLineEdit {{
    background-color: {COLORS['card_alt']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    padding: 8px 12px;
    color: {COLORS['text']};
}}
QLineEdit:focus {{
    border: 1px solid {COLORS['accent']};
}}

QTableWidget {{
    background-color: {COLORS['card']};
    border: 1px solid {COLORS['border']};
    border-radius: 10px;
    gridline-color: {COLORS['border']};
    selection-background-color: {COLORS['accent_dim']};
}}
QHeaderView::section {{
    background-color: {COLORS['card_alt']};
    color: {COLORS['text_dim']};
    padding: 8px;
    border: none;
    font-weight: 600;
}}
"""


def apply_shadow(widget, blur=24, y_offset=6, alpha=110):
    """Elevation shadow — Qt Style Sheets don't support box-shadow, so this is
    the standard PySide6 way to fake elevated cards."""
    shadow = QGraphicsDropShadowEffect(widget)
    shadow.setBlurRadius(blur)
    shadow.setOffset(0, y_offset)
    shadow.setColor(Qt.GlobalColor.black)
    widget.setGraphicsEffect(shadow)


# ============================================================
#  REUSABLE WIDGETS
# ============================================================

class Card(QFrame):
    """Base rounded card container used everywhere in the dashboard."""

    def __init__(self, padding=18):
        super().__init__()
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {COLORS['card']};
                border: 1px solid {COLORS['border']};
                border-radius: 14px;
            }}
        """)
        self.layout_ = QVBoxLayout(self)
        self.layout_.setContentsMargins(padding, padding, padding, padding)
        apply_shadow(self)


class StatCard(Card):
    """Top-row summary tile: icon, label, big value, small delta."""

    def __init__(self, icon, title, value, delta, delta_positive=True):
        super().__init__()
        icon_lbl = QLabel(icon)
        icon_lbl.setStyleSheet("font-size: 22px; background: transparent;")

        title_lbl = QLabel(title)
        title_lbl.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 13px; background: transparent;")

        top_row = QHBoxLayout()
        top_row.addWidget(icon_lbl)
        top_row.addWidget(title_lbl)
        top_row.addStretch()

        value_lbl = QLabel(value)
        value_lbl.setStyleSheet("font-size: 26px; font-weight: 700; background: transparent;")

        delta_color = COLORS['accent'] if delta_positive else COLORS['danger']
        delta_lbl = QLabel(delta)
        delta_lbl.setStyleSheet(f"color: {delta_color}; font-size: 12px; font-weight: 600; background: transparent;")

        self.layout_.addLayout(top_row)
        self.layout_.addSpacing(6)
        self.layout_.addWidget(value_lbl)
        self.layout_.addWidget(delta_lbl)


class SidebarButton(QPushButton):
    """Checkable nav button used in the left rail."""

    def __init__(self, icon, text):
        super().__init__(f"  {icon}   {text}")
        self.setCheckable(True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFixedHeight(44)
        self.setStyleSheet(f"""
            QPushButton {{
                text-align: left;
                background-color: transparent;
                color: {COLORS['text_dim']};
                border: none;
                border-radius: 10px;
                font-size: 14px;
                padding-left: 6px;
            }}
            QPushButton:hover {{
                background-color: {COLORS['card_alt']};
                color: {COLORS['text']};
            }}
            QPushButton:checked {{
                background-color: {COLORS['accent_dim']};
                color: #052A20;
                font-weight: 700;
            }}
        """)


class IntegrationButton(QPushButton):
    """Quick-launch button wired straight to a GoogleFuncs / MicrosoftFuncs
    static method — clicking it opens the real web app in the browser."""

    def __init__(self, icon, label, handler):
        super().__init__(f"{icon}   {label}")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFixedHeight(46)
        self.setStyleSheet(f"""
            QPushButton {{
                text-align: left;
                background-color: {COLORS['card_alt']};
                border: 1px solid {COLORS['border']};
                border-radius: 10px;
                padding-left: 14px;
                font-size: 13px;
                font-weight: 600;
                color: {COLORS['text']};
            }}
            QPushButton:hover {{
                border: 1px solid {COLORS['accent']};
                color: {COLORS['accent']};
            }}
        """)
        self.clicked.connect(handler)


def budget_bar(percent, label, spent, limit):
    """Returns a small widget: category name, colored progress bar, amounts."""
    wrap = QWidget()
    wrap.setStyleSheet("background: transparent;")
    v = QVBoxLayout(wrap)
    v.setContentsMargins(0, 0, 0, 0)
    v.setSpacing(4)

    top = QHBoxLayout()
    name = QLabel(label)
    name.setStyleSheet("font-size: 13px; font-weight: 600; background: transparent;")
    amounts = QLabel(f"₹{spent:,} / ₹{limit:,}")
    amounts.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 12px; background: transparent;")
    top.addWidget(name)
    top.addStretch()
    top.addWidget(amounts)

    bar = QProgressBar()
    bar.setRange(0, 100)
    bar.setValue(percent)
    bar.setTextVisible(False)
    bar.setFixedHeight(8)

    color = COLORS['accent']
    if percent >= 90:
        color = COLORS['danger']
    elif percent >= 70:
        color = COLORS['warning']

    bar.setStyleSheet(f"""
        QProgressBar {{
            background-color: {COLORS['border']};
            border-radius: 4px;
        }}
        QProgressBar::chunk {{
            background-color: {color};
            border-radius: 4px;
        }}
    """)

    v.addLayout(top)
    v.addWidget(bar)
    return wrap


# ============================================================
#  PAGES
# ============================================================

class DashboardPage(QWidget):
    def __init__(self, username):
        super().__init__()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addWidget(scroll)
        scroll.setWidget(inner)

        layout = QVBoxLayout(inner)
        layout.setContentsMargins(28, 24, 28, 28)
        layout.setSpacing(20)

        # ---- stat cards row ----
        stats_row = QHBoxLayout()
        stats_row.setSpacing(16)
        stats_row.addWidget(StatCard("💰", "Total Balance", "₹1,24,500", "▲ 4.2% this month", True))
        stats_row.addWidget(StatCard("📈", "Income", "₹85,000", "▲ 2.1% vs last month", True))
        stats_row.addWidget(StatCard("📉", "Spent", "₹32,180", "▼ 6.4% vs last month", True))
        stats_row.addWidget(StatCard("🎯", "Savings Rate", "62%", "On track for goal", True))
        layout.addLayout(stats_row)

        # ---- middle: budget overview + integrations ----
        mid_row = QHBoxLayout()
        mid_row.setSpacing(16)

        budget_card = Card()
        budget_title = QLabel("Budget Overview")
        budget_title.setStyleSheet("font-size: 16px; font-weight: 700; background: transparent;")
        budget_card.layout_.addWidget(budget_title)
        budget_card.layout_.addSpacing(10)
        budget_card.layout_.addWidget(budget_bar(72, "Food & Groceries", 7200, 10000))
        budget_card.layout_.addSpacing(14)
        budget_card.layout_.addWidget(budget_bar(45, "Transport", 2250, 5000))
        budget_card.layout_.addSpacing(14)
        budget_card.layout_.addWidget(budget_bar(91, "Entertainment", 2730, 3000))
        budget_card.layout_.addSpacing(14)
        budget_card.layout_.addWidget(budget_bar(30, "Bills & Utilities", 1500, 5000))
        budget_card.layout_.addStretch()

        integ_card = Card()
        integ_title = QLabel("Quick Integrations")
        integ_title.setStyleSheet("font-size: 16px; font-weight: 700; background: transparent;")
        integ_sub = QLabel("Jump straight into your workspace")
        integ_sub.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 12px; background: transparent;")
        integ_card.layout_.addWidget(integ_title)
        integ_card.layout_.addWidget(integ_sub)
        integ_card.layout_.addSpacing(10)
        integ_card.layout_.addWidget(IntegrationButton("📊", "Google Sheets", GoogleFuncs.open_sheets))
        integ_card.layout_.addWidget(IntegrationButton("📄", "Google Docs", GoogleFuncs.open_docs))
        integ_card.layout_.addWidget(IntegrationButton("📈", "Microsoft Excel", MicrosoftFuncs.open_excel))
        integ_card.layout_.addWidget(IntegrationButton("📅", "Google Calendar", GoogleFuncs.open_calendar))
        integ_card.layout_.addStretch()

        mid_row.addWidget(budget_card, 3)
        mid_row.addWidget(integ_card, 2)
        layout.addLayout(mid_row)

        # ---- recent activity ----
        activity_card = Card()
        activity_title = QLabel("Recent Activity")
        activity_title.setStyleSheet("font-size: 16px; font-weight: 700; background: transparent;")
        activity_card.layout_.addWidget(activity_title)
        activity_card.layout_.addSpacing(8)

        empty_state = QLabel("No transactions logged yet — connect a data source or add one manually to get started.")
        empty_state.setWordWrap(True)
        empty_state.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 13px; background: transparent; padding: 20px 0;")
        activity_card.layout_.addWidget(empty_state)

        layout.addWidget(activity_card)
        layout.addStretch()


class ProfilePage(QWidget):
    def __init__(self, username):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 28)
        layout.setSpacing(18)

        card = Card()
        header = QHBoxLayout()

        avatar = QLabel(username[:1].upper() if username else "F")
        avatar.setFixedSize(64, 64)
        avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        avatar.setStyleSheet(f"""
            background-color: {COLORS['accent']};
            color: #052A20;
            border-radius: 32px;
            font-size: 26px;
            font-weight: 700;
        """)

        name_box = QVBoxLayout()
        name_lbl = QLabel(username or "Guest")
        name_lbl.setStyleSheet("font-size: 20px; font-weight: 700; background: transparent;")
        role_lbl = QLabel("Fintraa User")
        role_lbl.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 13px; background: transparent;")
        name_box.addWidget(name_lbl)
        name_box.addWidget(role_lbl)

        header.addWidget(avatar)
        header.addSpacing(14)
        header.addLayout(name_box)
        header.addStretch()

        card.layout_.addLayout(header)
        card.layout_.addSpacing(20)

        for field_label, placeholder in [
            ("Full Name", username or "Guest"),
            ("Email", "you@example.com"),
            ("Preferred Currency", "INR (₹)"),
            ("Member Since", datetime.now().strftime("%d %b %Y")),
        ]:
            lbl = QLabel(field_label)
            lbl.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 12px; background: transparent;")
            field = QLineEdit()
            field.setText(placeholder)
            card.layout_.addWidget(lbl)
            card.layout_.addWidget(field)
            card.layout_.addSpacing(10)

        layout.addWidget(card)
        layout.addStretch()


class SpentPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 28)
        layout.setSpacing(16)

        top_row = QHBoxLayout()
        title = QLabel("Expenses")
        title.setStyleSheet("font-size: 20px; font-weight: 700; background: transparent;")
        add_btn = QPushButton("+  Add Expense")
        add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        add_btn.setFixedHeight(38)
        add_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['accent']};
                color: #052A20;
                border-radius: 8px;
                padding: 0 16px;
                font-weight: 700;
            }}
            QPushButton:hover {{ background-color: {COLORS['accent_dim']}; }}
        """)
        top_row.addWidget(title)
        top_row.addStretch()
        top_row.addWidget(add_btn)
        layout.addLayout(top_row)

        table = QTableWidget(0, 4)
        table.setHorizontalHeaderLabels(["Date", "Category", "Description", "Amount"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        layout.addWidget(table)


class BudgetPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 28)
        layout.setSpacing(16)

        title = QLabel("Budget Planner")
        title.setStyleSheet("font-size: 20px; font-weight: 700; background: transparent;")
        layout.addWidget(title)

        card = Card()
        card.layout_.addWidget(budget_bar(72, "Food & Groceries", 7200, 10000))
        card.layout_.addSpacing(16)
        card.layout_.addWidget(budget_bar(45, "Transport", 2250, 5000))
        card.layout_.addSpacing(16)
        card.layout_.addWidget(budget_bar(91, "Entertainment", 2730, 3000))
        card.layout_.addSpacing(16)
        card.layout_.addWidget(budget_bar(30, "Bills & Utilities", 1500, 5000))
        card.layout_.addSpacing(16)
        card.layout_.addWidget(budget_bar(58, "Savings Goal", 11600, 20000))
        layout.addWidget(card)
        layout.addStretch()


class IntegrationsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 28)
        layout.setSpacing(16)

        title = QLabel("Integrations")
        title.setStyleSheet("font-size: 20px; font-weight: 700; background: transparent;")
        layout.addWidget(title)

        row = QHBoxLayout()
        row.setSpacing(16)

        google_card = Card()
        g_title = QLabel("🟦  Google Workspace")
        g_title.setStyleSheet("font-size: 15px; font-weight: 700; background: transparent;")
        google_card.layout_.addWidget(g_title)
        google_card.layout_.addSpacing(10)
        google_card.layout_.addWidget(IntegrationButton("📊", "Sheets", GoogleFuncs.open_sheets))
        google_card.layout_.addWidget(IntegrationButton("📄", "Docs", GoogleFuncs.open_docs))
        google_card.layout_.addWidget(IntegrationButton("🖼", "Slides", GoogleFuncs.open_slides))
        google_card.layout_.addWidget(IntegrationButton("📅", "Calendar", GoogleFuncs.open_calendar))
        google_card.layout_.addStretch()

        ms_card = Card()
        m_title = QLabel("🟩  Microsoft 365")
        m_title.setStyleSheet("font-size: 15px; font-weight: 700; background: transparent;")
        ms_card.layout_.addWidget(m_title)
        ms_card.layout_.addSpacing(10)
        ms_card.layout_.addWidget(IntegrationButton("📈", "Excel", MicrosoftFuncs.open_excel))
        ms_card.layout_.addWidget(IntegrationButton("📝", "Word", MicrosoftFuncs.open_word))
        ms_card.layout_.addWidget(IntegrationButton("📽", "PowerPoint", MicrosoftFuncs.open_powerpoint))
        ms_card.layout_.addWidget(IntegrationButton("🧩", "Microsoft 365", MicrosoftFuncs.open_365))
        ms_card.layout_.addStretch()

        row.addWidget(google_card)
        row.addWidget(ms_card)
        layout.addLayout(row)
        layout.addStretch()


# ============================================================
#  MAIN WINDOW
# ============================================================

class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username or "Guest"
        self.setWindowTitle("Fintraa — Smart Finance Suite")
        self.resize(1280, 800)
        self.setMinimumSize(1040, 680)

        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(self._build_sidebar())

        right = QVBoxLayout()
        right.setContentsMargins(0, 0, 0, 0)
        right.setSpacing(0)
        right.addWidget(self._build_header())
        right.addWidget(self._build_pages())

        right_wrap = QWidget()
        right_wrap.setLayout(right)
        root.addWidget(right_wrap)

    # -------------------- sidebar --------------------
    def _build_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(230)
        sidebar.setStyleSheet(f"""
            QFrame {{
                background-color: {COLORS['sidebar']};
                border-right: 1px solid {COLORS['border']};
            }}
        """)
        v = QVBoxLayout(sidebar)
        v.setContentsMargins(18, 24, 18, 18)
        v.setSpacing(4)

        brand = QLabel('<span style="color:#E7ECF5;">Fin</span><span style="color:#2FE6A6;">traa</span>')
        brand.setStyleSheet("font-size: 22px; font-weight: 800; background: transparent;")
        subtitle = QLabel("Smart Finance Suite")
        subtitle.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 11px; background: transparent;")

        v.addWidget(brand)
        v.addWidget(subtitle)
        v.addSpacing(28)

        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        nav_items = [
            ("🏠", "Dashboard", 0),
            ("👤", "Profile", 1),
            ("💸", "Spent", 2),
            ("🎯", "Budget", 3),
            ("🔗", "Integrations", 4),
        ]
        self.nav_buttons = {}
        for icon, label, index in nav_items:
            btn = SidebarButton(icon, label)
            btn.clicked.connect(lambda checked, i=index: self.stack.setCurrentIndex(i))
            self.nav_group.addButton(btn)
            v.addWidget(btn)
            self.nav_buttons[index] = btn
        self.nav_buttons[0].setChecked(True)

        v.addStretch()

        # bottom mini profile
        divider = QFrame()
        divider.setFixedHeight(1)
        divider.setStyleSheet(f"background-color: {COLORS['border']};")
        v.addWidget(divider)
        v.addSpacing(10)

        founder = QLabel(f"👑  {self.username}")
        founder.setStyleSheet("font-size: 13px; font-weight: 600; background: transparent;")
        role = QLabel("CEO & Founder")
        role.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 11px; background: transparent;")
        v.addWidget(founder)
        v.addWidget(role)

        return sidebar

    # -------------------- header --------------------
    def _build_header(self):
        header = QFrame()
        header.setFixedHeight(84)
        header.setStyleSheet(f"""
            QFrame {{
                background-color: {COLORS['bg']};
                border-bottom: 1px solid {COLORS['border']};
            }}
        """)
        h = QHBoxLayout(header)
        h.setContentsMargins(28, 0, 28, 0)

        left = QVBoxLayout()
        greeting = QLabel(self._greeting())
        greeting.setStyleSheet("font-size: 18px; font-weight: 700; background: transparent;")
        quote = QLabel(f"“{quote_of_the_day()}”")
        quote.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 12px; font-style: italic; background: transparent;")
        left.addWidget(greeting)
        left.addWidget(quote)

        h.addLayout(left)
        h.addStretch()

        badges = QHBoxLayout()
        badges.setSpacing(10)
        badges.addWidget(self._badge("🌤", "27°C · Light Rain"))
        badges.addWidget(self._badge("📅", datetime.now().strftime("%d.%m.%Y")))
        h.addLayout(badges)

        return header

    def _badge(self, icon, text):
        b = QLabel(f"{icon}  {text}")
        b.setStyleSheet(f"""
            background-color: {COLORS['card_alt']};
            border: 1px solid {COLORS['border']};
            border-radius: 8px;
            padding: 8px 14px;
            font-size: 12px;
            color: {COLORS['text_dim']};
        """)
        return b

    def _greeting(self):
        hour = datetime.now().hour
        part = "morning" if hour < 12 else "afternoon" if hour < 18 else "evening"
        return f"Good {part}, {self.username} 👋"

    # -------------------- pages --------------------
    def _build_pages(self):
        self.stack = QStackedWidget()
        self.stack.addWidget(DashboardPage(self.username))
        self.stack.addWidget(ProfilePage(self.username))
        self.stack.addWidget(SpentPage())
        self.stack.addWidget(BudgetPage())
        self.stack.addWidget(IntegrationsPage())
        return self.stack


# ============================================================
#  ENTRY POINT
# ============================================================

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET)

    # Same idea as the original console prototype's `information()` step —
    # ask for the user's name once at launch.
    name, ok = QInputDialog.getText(None, "Welcome to Fintraa", "Enter your name:")
    if not ok or not name.strip():
        name = "Guest"

    window = MainWindow(name.strip())
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
