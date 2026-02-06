import flet as ft
from api_client import APIClient


class PredictionApp:

    def __init__(self, page: ft.Page):

        self.page = page
        self.api = APIClient()

        # ===== Page Setup =====
        self.page.title = "Machine Learning Process Predictor"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = "#020617"
        self.page.horizontal_alignment = "center"
        self.page.vertical_alignment = "center"

        # ===== Inputs =====
        self.p_pdg = self.create_field("P-PDG", "eg, 100")
        self.t_tpt = self.create_field("T-TPT", "eg, 50")
        self.t_jus_ckp = self.create_field("T-JUS-CKP", "eg, 30")
        self.p_tpt = self.create_field("P-TPT", "eg, 120")
        self.p_mon_ckp = self.create_field("P-MON-CKP", "eg, 80")

        # ===== Result =====
        self.result_text = ft.Text(
            "N/A",
            size=34,
            weight="bold",
            color="#60a5fa",
            animate_opacity=300,
            animate_scale=300,
        )

        # ===== Loader =====
        self.loader = ft.ProgressRing(visible=False)

        # ===== Button =====
        self.predict_btn = ft.ElevatedButton(
            "PREDICT CLASS",
            on_click=self.on_predict,
            on_hover=self.on_hover_btn,
            style=ft.ButtonStyle(
                bgcolor="#2563eb",
                color="white",
                padding=22,
                elevation=12,
                shape=ft.RoundedRectangleBorder(radius=20),
            ),
        )

        self.build_ui()

    # -------------------------------------------------
    # Field Creator
    # -------------------------------------------------
    def create_field(self, label, hint):

        tf = ft.TextField(
            label=label,
            hint_text=hint,
            width=420,
            keyboard_type=ft.KeyboardType.NUMBER,
            border_radius=20,
            filled=True,
            bgcolor="#020617AA",
            animate_scale=200,
            on_change=self.on_change,
            on_focus=self.on_focus,
            on_blur=self.on_blur,
        )

        return tf

    # -------------------------------------------------
    # Sensor Card (Hover Glow)
    # -------------------------------------------------
    def create_sensor_card(self, title, desc):

        card = ft.Container(
            padding=18,
            border_radius=18,
            bgcolor="#020617AA",
            border=ft.border.all(1, "#1e293b"),
            animate=200,
            on_hover=self.on_sensor_hover,
            content=ft.Column(
                [
                    ft.Text(title, weight="bold", size=16, color="#60a5fa"),
                    ft.Text(desc, size=13, color="white70"),
                ],
                spacing=6,
            ),
        )

        return card

    def on_sensor_hover(self, e):

        if e.data == "true":
            e.control.border = ft.border.all(1.5, "#38bdf8")
            e.control.scale = 1.02
        else:
            e.control.border = ft.border.all(1, "#1e293b")
            e.control.scale = 1

        self.page.update()

    # -------------------------------------------------
    # Animations
    # -------------------------------------------------
    def on_focus(self, e):
        e.control.scale = 1.02
        self.page.update()

    def on_blur(self, e):
        e.control.scale = 1
        self.page.update()

    def on_change(self, e):

        field = e.control

        try:
            if field.value:
                float(field.value)
                field.border_color = "#38bdf8"
            else:
                field.border_color = None
        except:
            field.border_color = "#ef4444"

        self.page.update()

    def on_hover_btn(self, e):
        if e.data == "true":
            self.predict_btn.style.bgcolor = "#3b82f6"
            self.predict_btn.scale = 1.05
        else:
            self.predict_btn.style.bgcolor = "#2563eb"
            self.predict_btn.scale = 1

        self.page.update()

    # -------------------------------------------------
    # UI Layout
    # -------------------------------------------------
    def build_ui(self):

        # ===== LEFT FORM =====
        form_glass = ft.Container(
            padding=45,
            border_radius=30,
            bgcolor="#0f172a88",
            blur=22,
            border=ft.border.all(1, "#334155"),
            content=ft.Column(
                [
                    ft.Text(
                        "Machine Learning Process Predictor",
                        size=34,
                        weight="bold",
                        color="white",
                    ),

                    self.p_pdg,
                    self.t_tpt,
                    self.t_jus_ckp,
                    self.p_tpt,
                    self.p_mon_ckp,

                    self.predict_btn,
                    self.loader,

                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text("Status:", color="white"),
                                self.result_text,
                            ],
                            alignment="spaceBetween",
                        ),
                        border_radius=20,
                        padding=22,
                        bgcolor="#020617AA",
                        border=ft.border.all(1, "#1e293b"),
                        width=420,
                    ),
                ],
                spacing=24,
                horizontal_alignment="center",
            ),
        )

        # ===== RIGHT SENSOR PANEL =====
        sensor_panel = ft.Container(
            width=430,
            padding=30,
            border_radius=30,
            bgcolor="#0f172a88",
            blur=22,
            border=ft.border.all(1, "#334155"),
            content=ft.Column(
                [
                    ft.Text("Sensors Overview", size=26, weight="bold", color="white"),

                    self.create_sensor_card(
                        "P-PDG | Downhole Pressure",
                        "Monitors reservoir pressure at the well bottom to track depletion and flow potential.",
                    ),

                    self.create_sensor_card(
                        "T-TPT | Tubing Temperature",
                        "Measures surface fluid temperature to prevent pipe blockages and monitor flow consistency.",
                    ),

                    self.create_sensor_card(
                        "T-JUS-CKP | Pre-Choke Temp",
                        "Tracks fluid temperature right before the choke valve to ensure equipment safety.",
                    ),

                    self.create_sensor_card(
                        "P-TPT | Tubing Pressure",
                        "The main indicator of a well's surface pressure and overall production health.",
                    ),

                    self.create_sensor_card(
                        "P-MON-CKP | Post-Choke Pressure",
                        "Measures pressure after the control valve to calculate flow rates and pressure drops.",
                    ),
                ],
                spacing=14,
            ),
        )

        # ===== MAIN LAYOUT =====
        self.page.add(
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#020617", "#020617", "#0f172a"],
                ),
                content=ft.Row(
                    [form_glass, sensor_panel],
                    alignment="center",
                    vertical_alignment="center",
                    spacing=40,
                ),
            )
        )

    # -------------------------------------------------
    # Predict Logic
    # -------------------------------------------------
    def on_predict(self, e):

        try:
            data = {
                "P_PDG": float(self.p_pdg.value),
                "T_TPT": float(self.t_tpt.value),
                "T_JUS_CKP": float(self.t_jus_ckp.value),
                "P_TPT": float(self.p_tpt.value),
                "P_MON_CKP": float(self.p_mon_ckp.value),
            }
        except:
            self.result_text.value = "INVALID INPUT"
            self.page.update()
            return

        self.predict_btn.disabled = True
        self.loader.visible = True
        self.page.update()

        prediction = self.api.predict(data)

        self.result_text.opacity = 0
        self.result_text.scale = 0.7
        self.page.update()

        self.result_text.value = prediction
        self.loader.visible = False
        self.predict_btn.disabled = False

        self.result_text.opacity = 1
        self.result_text.scale = 1

        self.page.update()


def main(page: ft.Page):
    PredictionApp(page)


ft.app(target=main)
