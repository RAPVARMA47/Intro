import streamlit as st 

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def main():
    
        st.write("""<h2 style='color: #2c3e50; text-align: center;'>Your Trusted Legal Assistant</h2>""", unsafe_allow_html=True)
        st.write(
            """
            <div style='text-align: justify; font-size: 16px; color: #34495e;'>
                Welcome to <strong>Legal Bot </strong>, your trusted partner in navigating the complexities of legal documentation. 
                Whether you're drafting contracts, agreements, or any other legal documents, we are here to simplify the process and ensure precision in every detail.
                As legal professionals, we understand that the smallest mistake in a document can have significant implications. 
                Our advanced AI-powered tools are designed to assist you with drafting, reviewing, and finalizing your legal documents, 
                ensuring that you never miss a critical detail.<br><br>
                With <strong>Legal Bot</strong>, 
                <ul>
                    <li>Generate accurate and comprehensive legal documents with ease.</li>
                    <li>Fill in placeholders with confidence, knowing that every detail is meticulously handled.</li>
                    <li>Review and finalize your drafts quickly, saving valuable time and resources.</li>
                </ul><br>
                Our platform combines the power of cutting-edge AI technology with the knowledge of seasoned legal professionals, 
                offering you a reliable assistant that adapts to your specific needs. Whether you're an individual, a law firm, or a corporation, 
                <strong>Legal Bot</strong> is here to enhance your productivity and ensure the highest standards of legal accuracy.
                Step into the future of legal document management with <strong>Legal Bot</strong>. Let us handle the details, 
                so you can focus on what truly matters – providing exceptional legal services to your clients.
            </div>                  
            """,
            unsafe_allow_html=True
        )
        
if __name__==  "__main__":
    main()