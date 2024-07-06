
# YAAN Platform

The Youth Activists Association of Nigeria (YAAN) Platform is a web application designed to facilitate communication, coordination, and activism among Nigerian citizens and volunteers. This platform aims to bring together people from all walks of life to work towards positive change in Nigeria. 

### Technologies Used

- **Backend**: Python Django Framework
- **Frontend**: React, HTML, CSS, JavaScript
- **Real-Time Communication**: WebRTC

### User Types

There are two main types of users on the YAAN Platform:

1. **Users**: General members of the public who can participate in polls, view events, and interact with posts made by volunteers.
2. **Volunteers**: Active members who can create posts, participate in chat discussions, organize events, and engage in live chat sessions.

### Features and Components

1. **Polls**: 
    - Users can participate in polls created by volunteers.
    - Polls help gather opinions and insights on various issues.

2. **Events**: 
    - Volunteers can create and manage events.
    - Users can view and RSVP to events.

3. **Chat**:
    - Dedicated chat functionality for communication between volunteers.
    - Facilitates coordination and discussion among active members.

4. **Posts**:
    - Only volunteers can create posts.
    - Users can like or dislike posts, fostering engagement and feedback.

5. **Live Chat**:
    - Real-time chat functionality for volunteers using WebRTC.
    - Enables immediate communication and collaboration.

### Future Enhancements

While the current functionality covers the essential needs of the platform, the following features are considered for future updates:

1. **User Registration and Profile Management**:
    - Enhanced user profiles with more personal information and customization options.
    - Profile pictures and bio sections for better community building.

2. **Volunteer Application and Management**:
    - Streamlined process for users to apply as volunteers.
    - Volunteer management tools for administrators to track and assign tasks.

3. **Notifications System**:
    - Real-time notifications for new polls, events, posts, and messages.
    - Email notifications for important updates.

4. **Content Moderation**:
    - Moderation tools for administrators to ensure compliance with community guidelines.
    - Reporting mechanisms for inappropriate content.

5. **Resource Library**:
    - A section for educational materials, documents, and resources related to activism and governance.
    - Upload and download functionality for documents and multimedia.

6. **Forums or Discussion Boards**:
    - Public and private forums for users to discuss various topics.
    - Moderated by volunteers or administrators.

7. **Event Management Enhancements**:
    - Calendar view for events.
    - Event reminders and RSVPs tracking.

8. **Advanced Polling Features**:
    - Anonymous polling options.
    - Detailed results and analytics for each poll.

9. **Analytics Dashboard**:
    - Dashboard for administrators to track user engagement, poll results, event participation, and more.

10. **Multilingual Support**:
    - Support for multiple languages to accommodate Nigeria's diverse population.

### Contributing

We welcome contributions from the community to help improve and expand the YAAN Platform. If you're interested in contributing, please follow the steps below:

1. **Fork the Repository**: Create a personal fork of the repository on GitHub.
2. **Clone the Repository**: Clone your fork to your local machine using `git clone`.
3. **Create a Branch**: Create a new branch for your feature or bug fix.
4. **Make Changes**: Implement your changes and commit them to your branch.
5. **Push to GitHub**: Push your changes to your fork on GitHub.
6. **Create a Pull Request**: Submit a pull request to the main repository.

### Setup Instructions

To set up the YAAN Platform locally, follow these steps:

1. **Clone the Repository**: 
    \`\`\`bash
    git clone https://github.com/yourusername/YAAN-Platform.git
    cd YAAN-Platform
    \`\`\`

2. **Backend Setup**:
    - Ensure you have Python and Django installed.
    - Navigate to the backend directory and install the required dependencies:
        \`\`\`bash
        pip install -r requirements.txt
        \`\`\`
    - Run the Django development server:
        \`\`\`bash
        python manage.py runserver
        \`\`\`

3. **Frontend Setup**:
    - Ensure you have Node.js and npm installed.
    - Navigate to the frontend directory and install the required dependencies:
        \`\`\`bash
        npm install
        \`\`\`
    - Start the React development server:
        \`\`\`bash
        npm start
        \`\`\`

4. **Access the Platform**:
    - Open your web browser and navigate to \`http://localhost:3000\` to access the frontend.
    - The backend will be running at \`http://localhost:8000\`.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any questions or suggestions, please contact us at info@yaan.org.
