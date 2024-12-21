# Sawm

Sawm is an advanced web application built using the Django framework, designed to deliver accurate Suhoor (pre-dawn meal) and Iftar (breaking the fast) timings tailored to user-specified inputs. This project showcases a modern, user-centric approach to web development, combining intuitive interface design with robust backend functionality to meet the needs of users observing fasting practices, particularly during Ramadan.

## Project Overview

The Sawm application is centered around a single Django app named home, which orchestrates the entire workflow—from capturing user inputs to making external API requests and rendering dynamic results. The project emphasizes modularity, scalability, and maintainability, ensuring it can adapt seamlessly to future enhancements.

### Key Features

- *Dynamic Input Form*: The primary user interface allows users to input essential details such as country, city, date, and the preferred calculation method for prayer timings.
- *API Integration*: The application leverages the Al-Adhan API, a trusted source for prayer timing data, to ensure precise and up-to-date results.
- *Template-Driven Rendering*: The Django templating engine enables dynamic content rendering, ensuring a consistent and responsive user experience across devices.
- *Custom Styling*: A dedicated styles.css file delivers an aesthetically pleasing and accessible interface.

## File Structure

### Templates

- *base.html*: This foundational template includes shared elements such as navigation and footer components. It provides a consistent structure for all other templates in the application.
- *index.html*: The main user interface, featuring a form where users provide their details. It serves as the entry point for generating Suhoor and Iftar timings.
- *displayTime.html*: Displays the fetched prayer timings in a clear and user-friendly format, styled for optimal readability and accessibility.

### Static Files

- *styles.css*: This file contains custom CSS rules that define the visual appearance of the application. It prioritizes a minimalistic design while ensuring the interface remains intuitive and engaging.

### Views

The views.py file encapsulates the application’s core functionality, bridging the front-end and back-end. Key features include:

1. *Input Validation*: Ensures all form fields are completed and validates the selected calculation method. Invalid inputs are flagged early to improve the user experience.
2. *API Interaction*: Constructs and executes requests to the Al-Adhan API using user-provided data. The API response is parsed to extract relevant Suhoor and Iftar timings.
3. *Response Formatting*: Formats the API response data into user-friendly time formats before passing it to the display template.
4. *Error Management*: Redirects users to an error page (error.html) with contextual messages when inputs are incomplete, invalid, or when the API encounters issues.

## Design Choices

### API Selection

The Al-Adhan API was chosen for its reliability, comprehensive dataset, and flexibility in accepting diverse input parameters such as country, city, and calculation method. This ensures that users receive precise and contextually relevant timings, enhancing the application's utility.

### Template and Styling Strategy

Django’s templating engine was selected for its ability to dynamically render content, ensuring a seamless integration between static and dynamic elements. A modular approach to template design ensures maintainability and scalability. The custom CSS stylesheet further enhances the aesthetic appeal, striking a balance between simplicity and functionality.

### Error Handling Framework

Robust error-handling mechanisms were implemented to ensure a smooth user experience. For instance, invalid form inputs or API-related errors prompt user-friendly error messages, preventing abrupt interruptions and guiding users toward corrective actions.

## Planned Enhancements

To enhance functionality and user engagement, several features are planned for future iterations of Sawm:

- *User Authentication*: Introducing a login system to allow users to save default preferences, such as location and calculation method, for a more personalized experience.
- *Ramadan Calendar*: Adding a feature that displays a detailed Ramadan calendar, listing daily Suhoor and Iftar timings for the entire month.
- *Localization Support*: Expanding the application's accessibility by supporting multiple languages, catering to a diverse global audience.
- *Enhanced UI/UX*: Iterative improvements to the user interface and experience, incorporating user feedback and modern design principles.

## Conclusion

Sawm exemplifies a meticulously crafted web application aimed at meeting the specific needs of users observing fasting practices. By leveraging Django’s powerful features and integrating a reliable API, the application ensures accurate and timely delivery of prayer timings. The project’s modular structure and design decisions reflect a commitment to scalability, maintainability, and user satisfaction.

The future roadmap includes exciting additions such as user authentication and a comprehensive Ramadan calendar, promising to further enrich the application’s functionality and appeal. As Sawm evolves, it aims to set a benchmark for similar applications in terms of precision, usability, and innovation.