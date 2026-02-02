import gradio as gr
from analyzer import check_eligibility

def process_resume(file_obj):
    """
    Wrapper function for Gradio to interface with the analyzer logic.
    """
    if file_obj is None:
        return 0, "INVALID RESUME FILE"
    
    # file_obj is a str path when type="filepath"
    return check_eligibility(file_obj)

# Create Gradio Interface
with gr.Blocks(title="Smart Resume Eligibility Analyzer") as app:
    gr.Markdown("# Smart Resume Eligibility Analyzer")
    gr.Markdown("Upload a resume file to check eligibility based on technical skills.")
    gr.Markdown("Supported formats: `.txt` (only .txt is processed), `.pdf`, `.doc`, `.docx`")
    
    with gr.Row():
        with gr.Column():
            # Input: File Upload
            file_input = gr.File(
                label="Upload Resume",
                file_types=[".txt", ".pdf", ".doc", ".docx"],
                type="filepath" # Ensures we get a path
            )
            submit_btn = gr.Button("Analyze Resume", variant="primary")
            
        with gr.Column():
            # Output: Skill Count and Status
            skill_count_output = gr.Textbox(label="Skill Count")
            status_output = gr.Textbox(label="Candidate Status")
    
    # Event Listener
    submit_btn.click(
        fn=process_resume,
        inputs=file_input,
        outputs=[skill_count_output, status_output]
    )

if __name__ == "__main__":
    app.launch()
