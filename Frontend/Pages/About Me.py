import streamlit as st


def about_me():
    st.title("About Me")

    # Add your image
    st.image("your_image_url_or_path.jpg", caption="Hi! I'm XYZ", use_column_width=True)

    # Introduction
    st.markdown(
        """
        Hi there! 👋 I'm XYZ, a passionate and creative individual with a love for technology and design.
        I believe in the power of creating intuitive and delightful user experiences.
        """
    )

    # Work Experience
    st.header("Work Experience")

    st.subheader("Software Developer | ABC Company | January 2020 - Present")
    st.write(
        """
        - Spearheaded the development of innovative software solutions.
        - Collaborated with cross-functional teams to deliver high-quality products.
        - Conducted code reviews and mentored junior developers.
        """
    )

    st.subheader("UI/UX Designer | XYZ Studio | June 2018 - December 2019")
    st.write(
        """
        - Designed user interfaces that prioritize user experience and visual appeal.
        - Conducted user research and usability testing to inform design decisions.
        - Collaborated with clients to bring their visions to life.
        """
    )

    # Personal Info
    st.header("About Me")

    st.write(
        """
        I thrive on turning complex problems into simple, beautiful, and intuitive solutions.
        My skill set includes software development, UI/UX design, and a passion for learning new technologies.
        Let's build something amazing together!
        """
    )

    # Social Links
    st.header("Connect with Me")

    st.markdown(
        """
        - [LinkedIn](your_linkedin_profile_url)
        - [Website](your_website_url)
        - [Twitter](your_twitter_profile_url)
        - [Resume](your_resume_pdf_url)
        """
    )

    # Closing Message
    st.header("Looking Forward to Digital Product School")

    st.write(
        """
        I am thrilled at the prospect of joining Digital Product School! 
        Excited to learn, collaborate, and create impactful digital products with fellow innovators.
        Let's embark on this journey together!
        """
    )

if __name__ == "__main__":
    about_me()
