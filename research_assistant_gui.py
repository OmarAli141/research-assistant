import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from research_assistant import ResearchAssistant
import threading

class ResearchAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Research Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        self.assistant = None
        self.is_processing = False
        
        # Create widgets first
        self.create_widgets()
        
        # Initialize the assistant
        self.initialize_assistant()
        
    def initialize_assistant(self):
        """Initialize the research assistant in a separate thread"""
        self.status_label.config(text="🔄 Initializing...")
        threading.Thread(target=self._init_assistant, daemon=True).start()
        
    def _init_assistant(self):
        """Initialize assistant in background"""
        try:
            self.assistant = ResearchAssistant()
            self.root.after(0, lambda: self.status_label.config(text="✅ Ready"))
        except Exception as e:
            self.root.after(0, lambda: self.status_label.config(text=f"❌ Error: {str(e)}"))
            messagebox.showerror("Initialization Error", 
                               f"Failed to initialize Research Assistant:\n{e}")
    
    def create_widgets(self):
        """Create and configure GUI widgets"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🔍 Research Assistant", 
                              font=('Arial', 24, 'bold'), 
                              bg='#2c3e50', fg='white')
        title_label.pack(pady=20)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Query input section
        input_frame = tk.LabelFrame(main_frame, text="Enter Your Research Question", 
                                   font=('Arial', 12, 'bold'), 
                                   bg='#f0f0f0', fg='#2c3e50',
                                   padx=15, pady=15)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.question_entry = tk.Entry(input_frame, font=('Arial', 11),
                                       bd=2, relief=tk.SOLID)
        self.question_entry.pack(fill=tk.X, pady=5)
        self.question_entry.bind('<Return>', lambda e: self.start_research())
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.search_button = tk.Button(button_frame, text="🔍 Research",
                                      font=('Arial', 12, 'bold'),
                                      bg='#3498db', fg='white',
                                      activebackground='#2980b9',
                                      cursor='hand2',
                                      command=self.start_research,
                                      relief=tk.FLAT,
                                      padx=20, pady=10)
        self.search_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_button = tk.Button(button_frame, text="🗑️ Clear",
                                     font=('Arial', 12),
                                     bg='#95a5a6', fg='white',
                                     activebackground='#7f8c8d',
                                     cursor='hand2',
                                     command=self.clear_results,
                                     relief=tk.FLAT,
                                     padx=20, pady=10)
        self.clear_button.pack(side=tk.LEFT)
        
        # Results section
        results_frame = tk.LabelFrame(main_frame, text="Research Report", 
                                     font=('Arial', 12, 'bold'), 
                                     bg='#f0f0f0', fg='#2c3e50',
                                     padx=15, pady=15)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.results_text = scrolledtext.ScrolledText(results_frame,
                                                     font=('Consolas', 10),
                                                     wrap=tk.WORD,
                                                     bg='white',
                                                     relief=tk.SOLID,
                                                     bd=2)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#34495e', height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, text="🔄 Initializing...", 
                                    font=('Arial', 10),
                                    bg='#34495e', fg='white',
                                    anchor=tk.W)
        self.status_label.pack(fill=tk.X, padx=10, pady=5)
    
    def start_research(self):
        """Start the research process"""
        if self.is_processing:
            messagebox.showwarning("Processing", 
                                  "A research query is already being processed. Please wait.")
            return
        
        question = self.question_entry.get().strip()
        
        if not question:
            messagebox.showwarning("Empty Query", "Please enter a research question!")
            return
        
        if not self.assistant:
            messagebox.showerror("Not Ready", "Research Assistant is not initialized yet. Please wait.")
            return
        
        # Disable button and clear previous results
        self.search_button.config(state=tk.DISABLED)
        self.is_processing = True
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Researching: {question}\n")
        self.results_text.insert(tk.END, "⏳ Searching the web...\n\n")
        self.status_label.config(text="🔄 Processing your request...")
        
        # Start research in separate thread
        threading.Thread(target=self._do_research, args=(question,), daemon=True).start()
    
    def _do_research(self, question):
        """Perform research in background thread"""
        try:
            report = self.assistant.research_topic(question)
            
            # Update UI in main thread
            self.root.after(0, self._display_results, report)
            
        except Exception as e:
            error_msg = str(e)
            self.root.after(0, self._show_error, error_msg)
    
    def _display_results(self, report):
        """Display research results in the text area"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, report)
        self.search_button.config(state=tk.NORMAL)
        self.is_processing = False
        self.status_label.config(text="✅ Research completed successfully")
    
    def _show_error(self, error_msg):
        """Display error message"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"❌ Error occurred:\n\n{error_msg}")
        self.search_button.config(state=tk.NORMAL)
        self.is_processing = False
        self.status_label.config(text="❌ Error during research")
        
        if "Connection refused" in error_msg or "localhost:11434" in error_msg:
            messagebox.showerror("Connection Error", 
                               "Ollama is not running.\n\n"
                               "Please start Ollama on localhost:11434 before using the Research Assistant.")
    
    def clear_results(self):
        """Clear the results text area"""
        self.results_text.delete(1.0, tk.END)
        self.question_entry.delete(0, tk.END)
        self.status_label.config(text="📝 Ready for new query")

def main():
    root = tk.Tk()
    app = ResearchAssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

