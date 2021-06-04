# Practical Python Project using Flask Micro Framework, June 04, 2021.

<!-- ASSIGNMENT INTRO -->
<br />
<p>
  <h3 align="center">Mini Python Project - 2021 FSSD Jan - Aug Batch, Canadian Business College, Toronto, CA</h3>
  <br />
  <h5 align="center">This project is a part of the Full-Stack Software Development Diploma with Canadian Business College, Toronto and Code Institute(https://codeinstitute.net/full-stack-software-development-diploma/)</h5>
  <br />
  <p align="center">
    In this project, I have built a frontend-app using the technologies that I have learned throughout Flask framework classes. This project is built based on the concept of as soccer club site, an application helps the user to browse through to know the club players including their profiles.
    <br />
    <br />
    <h3 align="center">
        <a href="https://practical-python-flask-project.herokuapp.com/">View Project</a>
    </h3>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#git-installation">GIT Installation</a></li>
        <li><a href="#git-usage">GIT Usage</a></li>
        <li><a href="#heroku-deployment">Heroku Deployment</a></li>
      </ul>
    </li>
    <li><a href="#coding-and-testing">Coding and Testing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#credits-and-acknowledgements">Credits and Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE Project -->

## About The Project

[Live Project](https://practical-python-flask-project.herokuapp.com/)

- User can browse through the application to know about the soccer club players details.

### Built With

- [Clean Blog template](https://startbootstrap.com/theme/clean-blog)
- [Flask & Jinja Templating](https://flask.palletsprojects.com/en/2.0.x/templating/)
- [fontawesome](https://fontawesome.com/)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

<!-- GETTING STARTED -->

## Getting Started

The project has the following file structure.

- data
  - team.json file
- templates
  - it has main files of coding
    - base.html
    - index.html
    - team.html
    - contact.html
- static
  - it has main files downloaded as startbootstrap.com template
  - custom files
    - /css/style.css
    - /img/
- run.py file
- requirements.txt
  - Records an environment’s current package list
- README.md

### Prerequisites

- A basic knowledge in the following is required.
  - CLI
  - Python
  - Bootstrap, CSS, HTML
  - Logic
  - GIT basic operations
  - Heroku Installation and Implementation

### GIT Installation

1. Get a GIT account at [https://github.com](https://github.com)
2. Create a repository

3. GIT init in the local machine
   ```sh
   git init
   ```
4. Add the files to GIT local machine
   ```sh
   git add .
   ```
5. Commit `commit`
   ```sh
   git commit -m "text_message"
   ```
6. Create a branch in the local
   ```sh
   git branch -M main
   ```
7. Remote add the repo
   ```sh
   git remote add origin https://github.com/your_username_/Project-Name.git
   ```
8. Push the files
   ```sh
   git push -u origin main
   ```

<!-- USAGE EXAMPLES -->

### GIT Usage

1. Add the files
   ```sh
   git add <filename>
   ```
2. Commit the change
   ```sh
   git commit -m "message"
   ```
3. Push the changes to the repo
   ```sh
   git push origin main
   ```

### Heroku Deployment

1. Create / Sign Up a Heroku Account at [https://www.heroku.com/](https://www.heroku.com/)
    - Sign In to Heroku account
    - create New App
2. Connect Git remote to Heroku
    - Get heroku url from Settings Tab Section
      ```sh
      git remote add heroku https://git.heroku.com/practical-python-flask-project.git
      ```
     - Here, chosen 'heroku' as the remote name. It can be any name of your choice, but devoid of other remote names the repo has!
3. Create and/or Use a 'requirements.txt' file
    - use pip freeze / pip3 freeze to redirect the output, the installed packages, to the file as it's content by creating the file
      ```sh
      pip3 freeze > requirements.txt
      ```
4. Create a Heroku 'Procfile'
    - Put the following line in the file
    ```sh
    web: python run.py
    ```
5. Create your config vars (key:value)
    - Go to Settings -> Config Vars -> Add each one
        - IP : YOUR_IP
        - PORT: 5000
        - SECRET_KEY: xxxxxxx
6. Deploy
    - Either use cli method 
        ```sh
        git push -u heroku main
        ```
    OR

    - Go to Deploy Tab Section
        - Deployment method -> App connected to GitHub
            - Select (search and find) github repository
        - Deploy Branch
        - You could set Automatic Deploys, for next each pushes to the GitHub
7. Check the Activity Tab for Successful deployments OR other wise, in case of FAIL for errors
8. Finally, Open App for running the app

## Coding and Testing

- On coding, each functionality as a unit is being logically designed, implemented, followed with it's
    - Unit testing and
    - Use case testing

<!-- LICENSE -->

## License

Distributed under the GIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Josy George - [@github](https://github.com/josygeorge/)

<!-- ACKNOWLEDGEMENTS -->

## Credits and Acknowledgements

- [Stack Overflow](https://stackoverflow.com)
- [Mozilla.Org](https://developer.mozilla.org/en-US/docs/Web/Guide/)
- [W3 Schools](https://www.w3schools.com)
- [Instructor's (Anmar Jarjees) Notes](https://github.com/anmarjarjees?tab=repositories)
- [Technical Content (LMS) Provider](https://codeinstitute.net/full-stack-software-development-diploma/)
- [Management - Canadian Business College](https://canadianbusinesscollege.com/)
