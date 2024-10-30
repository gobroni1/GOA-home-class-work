import customtkinter as ctk
import tkinter as tk
import json


class NodeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Node Connection App")
        self.geometry("900x600")

        # Create a canvas for nodes
        self.canvas = tk.Canvas(self, bg="#444444", borderwidth=0, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a sidebar for node details
        self.sidebar = ctk.CTkFrame(self, width=300, fg_color="#333333", corner_radius=0)
        self.sidebar.place(relx=1.0, rely=0.0, anchor='ne', relheight=1.0)
        self.sidebar.place_forget()  # Hide the sidebar initially

        # Sidebar Title
        self.sidebar_title = ctk.CTkLabel(self.sidebar, text="Node Details", font=("Arial", 16, "bold"))
        self.sidebar_title.pack(pady=10, padx=10)

        # Node Title Entry
        self.node_title = ctk.CTkEntry(self.sidebar, placeholder_text="Node Title", width=280)
        self.node_title.pack(pady=5, padx=10)

        # Node Textbox
        self.node_text = ctk.CTkTextbox(self.sidebar, wrap="word", width=280, height=200)
        self.node_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        # Button Frame
        button_frame = ctk.CTkFrame(self.sidebar)
        button_frame.pack(pady=10, padx=10, anchor="ne")

        # Save Button
        self.save_button = ctk.CTkButton(button_frame, text="Save", width=100, command=self.save_state)
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Hide Button
        self.hide_button = ctk.CTkButton(button_frame, text="Hide", width=100, command=self.toggle_sidebar)
        self.hide_button.pack(side=tk.LEFT, padx=5)

        # Show Sidebar Button on Canvas
        self.show_sidebar_button = ctk.CTkButton(self.canvas, text="Show Sidebar", width=100, command=self.show_sidebar)
        self.show_sidebar_button.place(relx=1.0, rely=1.0, anchor='se')

        self.sidebar_visible = False
        self.current_node = None
        self.connection_start_node = None
        self.temp_line = None
        self.lines = []
        self.nodes = {}

        # Bind events
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<B1-Motion>", self.move_node)
        self.canvas.bind("<Button-1>", self.select_node)
        self.bind("<Delete>", self.delete_node)  # Bind delete key event

        # Save and Load state
        self.load_state()

        # Update node details when title or text is changed
        self.node_title.bind("<FocusOut>", self.update_node_title)
        self.node_text.bind("<FocusOut>", self.update_node_text)

        # Bind Enter key for saving title and text
        self.node_title.bind("<Return>", self.update_node_title)
        self.node_text.bind("<Return>", self.update_node_text)

    def on_right_click(self, event):
        node = self.node_near_position(event.x, event.y)
        if node:
            if self.connection_start_node:
                self.complete_connection(node)
            else:
                self.start_connection(event, node)
        else:
            if not self.node_at_position(event.x, event.y):
                self.create_node(event)

    def create_node(self, event):
        x, y = event.x, event.y
        name = self.show_name_input_dialog()
        if name:  # Only create node if a valid name is returned
            node_id = self.canvas.create_rectangle(x, y, x + 100, y + 40, fill="#333333", outline="#555555", width=4, tags=("node",))
            text_id = self.canvas.create_text(x + 50, y + 20, text=name, fill="#ffffff", font=("Arial", 10, "bold"), tags=("node_text",))
            self.nodes[node_id] = {"name": name, "text": "", "text_id": text_id, "connections": []}
            self.canvas.tag_bind(node_id, "<Button-1>", self.select_node)
            self.canvas.tag_bind(text_id, "<Button-1>", self.select_node)

    def show_name_input_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Enter Node Name")
        dialog.geometry("300x180")
        dialog.configure(bg="#444444")
        dialog.attributes("-topmost", True)

        label = ctk.CTkLabel(dialog, text="Node Name:", text_color="white")
        label.pack(pady=10, padx=10)

        entry = ctk.CTkEntry(dialog, width=250)
        entry.pack(pady=10, padx=10)

        def submit():
            self.node_name = entry.get()
            dialog.destroy()

        def cancel():
            self.node_name = None
            dialog.destroy()

        button_frame = ctk.CTkFrame(dialog, width=250, height=50)
        button_frame.pack(pady=10, padx=10)

        submit_button = ctk.CTkButton(button_frame, text="Name", width=120, command=submit)
        submit_button.pack(side=tk.LEFT, padx=5)

        cancel_button = ctk.CTkButton(button_frame, text="Cancel", width=120, command=cancel)
        cancel_button.pack(side=tk.LEFT, padx=5)

        self.wait_window(dialog)
        return self.node_name

    def node_at_position(self, x, y):
        items = self.canvas.find_overlapping(x - 5, y - 5, x + 5, y + 5)
        for item in items:
            if item in self.nodes:
                return True
        return False

    def node_near_position(self, x, y, distance=50):
        """ Check if there's a node within a certain distance from the position (x, y). """
        for node in self.nodes:
            coords = self.canvas.coords(node)
            node_x1, node_y1, node_x2, node_y2 = coords
            if (node_x1 - distance <= x <= node_x2 + distance) and (node_y1 - distance <= y <= node_y2 + distance):
                return node
        return None

    def select_node(self, event):
        closest_items = self.canvas.find_closest(event.x, event.y)
        if not closest_items:
            return

        item = closest_items[0]
        if item in self.nodes:
            self.current_node = item
            self.node_title.delete(0, tk.END)
            self.node_text.delete("1.0", tk.END)
            self.node_title.insert(0, self.nodes[item]["name"])
            self.node_text.insert("1.0", self.nodes[item]["text"])
            self.show_sidebar()  # Ensure the sidebar is visible if needed

    def start_connection(self, event, node):
        self.connection_start_node = node
        self.temp_line = self.canvas.create_line(0, 0, 0, 0, fill="yellow", width=2, smooth=True)
        self.canvas.bind("<Motion>", self.update_temp_line)

    def update_temp_line(self, event):
        if self.temp_line:
            x1, y1 = self.get_facing_side_center(self.connection_start_node, event.x, event.y)
            self.canvas.coords(self.temp_line, x1, y1, event.x, event.y)

    def complete_connection(self, target_node):
        if self.connection_start_node and self.connection_start_node != target_node:
            x1, y1 = self.get_facing_side_center(self.connection_start_node, *self.canvas.coords(target_node)[:2])
            x2, y2 = self.get_facing_side_center(target_node, *self.canvas.coords(self.connection_start_node)[:2])
            line = self.canvas.create_line(x1, y1, x2, y2, fill="yellow", width=2, smooth=True, arrow=tk.LAST)
            self.nodes[self.connection_start_node]["connections"].append((target_node, line))
            self.nodes[target_node]["connections"].append((self.connection_start_node, line))

        if self.temp_line:
            self.canvas.delete(self.temp_line)
            self.temp_line = None

        self.connection_start_node = None
        self.canvas.unbind("<Motion>")

    def move_node(self, event):
        if self.current_node:
            x, y = event.x, event.y
            coords = self.canvas.coords(self.current_node)
            dx = x - (coords[0] + coords[2]) / 2
            dy = y - (coords[1] + coords[3]) / 2
            self.canvas.move(self.current_node, dx, dy)
            text_id = self.nodes[self.current_node]["text_id"]
            self.canvas.move(text_id, dx, dy)
            self.update_connections(self.current_node)

    def update_connections(self, node):
        for connected_node, line in self.nodes[node]["connections"]:
            # Get the side centers for both nodes
            x1, y1 = self.get_facing_side_center(node, *self.canvas.coords(connected_node)[:2])
            x2, y2 = self.get_facing_side_center(connected_node, *self.canvas.coords(node)[:2])
            self.canvas.coords(line, x1, y1, x2, y2)

    def get_facing_side_center(self, node, x2, y2):
        x1, y1, x3, y3 = self.canvas.coords(node)

        node_center_x = (x1 + x3) / 2
        node_center_y = (y1 + y3) / 2

        if abs(node_center_x - x2) > abs(node_center_y - y2):
            if x2 > node_center_x:
                return x3, node_center_y  # Right side center
            else:
                return x1, node_center_y  # Left side center
        else:
            if y2 > node_center_y:
                return node_center_x, y3  # Bottom side center
            else:
                return node_center_x, y1  # Top side center

    def delete_node(self, event):
        if self.current_node:
            for connected_node, line in self.nodes[self.current_node]["connections"]:
                self.canvas.delete(line)
                self.nodes[connected_node]["connections"] = [
                    conn for conn in self.nodes[connected_node]["connections"] if conn[0] != self.current_node
                ]
            self.canvas.delete(self.current_node)
            self.canvas.delete(self.nodes[self.current_node]["text_id"])
            del self.nodes[self.current_node]
            self.current_node = None

    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.place_forget()
        else:
            self.sidebar.place(relx=1.0, rely=0.0, anchor='ne', relheight=1.0)
        self.sidebar_visible = not self.sidebar_visible

    def show_sidebar(self):
        if not self.sidebar_visible:
            self.sidebar.place(relx=1.0, rely=0.0, anchor='ne', relheight=1.0)
            self.sidebar_visible = True

    def update_node_title(self, event=None):
        if self.current_node:
            new_title = self.node_title.get()
            self.canvas.itemconfig(self.nodes[self.current_node]["text_id"], text=new_title)
            self.nodes[self.current_node]["name"] = new_title

    def update_node_text(self, event=None):
        if self.current_node:
            new_text = self.node_text.get("1.0", tk.END).strip()
            self.nodes[self.current_node]["text"] = new_text

    def save_state(self):
        state = {
            "nodes": {},
        }

        for node_id, node_info in self.nodes.items():
            x1, y1, x2, y2 = self.canvas.coords(node_id)
            node_data = {
                "name": node_info["name"],
                "text": node_info["text"],
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
            }
            state["nodes"][node_id] = node_data

        with open("nodes.json", "w") as file:
            json.dump(state, file)

    def load_state(self):
        try:
            with open("nodes.json", "r") as file:
                state = json.load(file)

            for node_id, node_data in state["nodes"].items():
                node_id = self.canvas.create_rectangle(node_data["x1"], node_data["y1"], node_data["x2"], node_data["y2"], fill="#333333", outline="#555555", width=4, tags=("node",))
                text_id = self.canvas.create_text((node_data["x1"] + node_data["x2"]) / 2, (node_data["y1"] + node_data["y2"]) / 2, text=node_data["name"], fill="#ffffff", font=("Arial", 10, "bold"), tags=("node_text",))
                self.nodes[node_id] = {"name": node_data["name"], "text": node_data["text"], "text_id": text_id, "connections": []}
                self.canvas.tag_bind(node_id, "<Button-1>", self.select_node)
                self.canvas.tag_bind(text_id, "<Button-1>", self.select_node)

        except FileNotFoundError:
            pass


if __name__ == "__main__":
    app = NodeApp()
    app.mainloop()
