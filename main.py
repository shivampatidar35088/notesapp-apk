import json
import os
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar

class NotesApp(MDApp):
    def build(self):
        self.notes = self.load_notes()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        self.main_layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10)
        self.toolbar = MDTopAppBar(title="Notes", elevation=10, pos_hint={"top": 1})
        self.main_layout.add_widget(self.toolbar)

        self.input = MDTextField(hint_text="Write your note...", size_hint_x=1, mode="rectangle")
        self.main_layout.add_widget(self.input)

        self.save_btn = MDFillRoundFlatButton(text="💾 Save Note", pos_hint={"center_x": 0.5}, on_release=self.save_note)
        self.main_layout.add_widget(self.save_btn)

        self.scroll = MDScrollView()
        self.notes_box = MDBoxLayout(orientation='vertical', adaptive_height=True, spacing=10, padding=(10, 10))
        self.scroll.add_widget(self.notes_box)
        self.main_layout.add_widget(self.scroll)

        self.refresh_notes()
        return self.main_layout

    def save_note(self, instance):
        note = self.input.text.strip()
        if note:
            self.notes.append(note)
            self.input.text = ""
            self.save_notes_to_file()
            self.refresh_notes()

    def delete_note(self, note_text):
        if note_text in self.notes:
            self.notes.remove(note_text)
            self.save_notes_to_file()
            self.refresh_notes()

    def refresh_notes(self):
        self.notes_box.clear_widgets()
        if not self.notes:
            self.notes_box.add_widget(MDLabel(text="No notes yet.", halign="center", theme_text_color="Hint"))
        else:
            for note in self.notes:
                card = MDCard(orientation='horizontal', padding=10, size_hint_y=None, height=70, elevation=6)
                label = MDLabel(text=note, halign="left", theme_text_color="Primary")
                delete_btn = MDIconButton(icon="delete", theme_text_color="Error", on_release=lambda btn, n=note: self.delete_note(n))
                card.add_widget(label)
                card.add_widget(delete_btn)
                self.notes_box.add_widget(card)

    def save_notes_to_file(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)

    def load_notes(self):
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as f:
                return json.load(f)
        return []

NotesApp().run()
