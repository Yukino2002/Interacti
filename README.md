[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h2 align="center">Interacti</h2>
<div align="center">
  <a href="https://github.com/Yukino2002/Interacti">
    <img src="./logo.jpg" alt="Logo" width="80" height="80">
  </a>
</div>
  <p align="center">
    A computer vision virtual classroom application that leverages computer vision technology to provide an immersive and interactive learning environment for students and teachers in a remote setting.
    <br />
    <br />
    <a href="https://youtu.be/XMMmAgVsEFY">View Demo</a>
    ·
    <a href="https://github.com/Yukino2002/Interacti/issues">Report Bug</a>
    ·
    <a href="https://github.com/Yukino2002/Interacti/issues">Request Feature</a>
  </p>


<!-- TABLE OF CONTENTS -->
<details>
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Our application uses computer vision technology to create virtual classrooms with real-time interactions and machine learning models to generate transcripts of real-time writing. With a user-friendly tkinter GUI, this app enhances the virtual learning experience for teachers and students.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

<ul>
    <li>Python</li>
    <li>OpenCV</li>
    <li>Keras</li>
    <li>TensorFlow</li>
    <li>Tkinter</li>
    <li>MediaPipe</li>
</ul>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Before getting a local copy up, you must ensure that you have the necessary software required.

### Prerequisites

* <a href='https://www.python.org/downloads/'>Python</a>

### Installation

1. Clone the repo
   ```sh
   git clone
   ```
2. Create a virtual environment.
    ```
    python -m venv env
    ```
3. Activate the virtual environment.
    ```
    source env/bin/activate  # for Linux/MacOS
    env\Scripts\activate  # for Windows
    ```
4. Install the required packages.
    ```
    pip install -r requirements.txt
    ```
5. (Optional) If you wish to train the model yourself, the dataset will be given below, the file is handwriting_model_train.ipynb.
6. Run the GUI using the command below.
    ```
    python frontend.py
    ```
   
### Dataset

The dataset used for training the ML model can be found 
<a href='https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format'>here</a>.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

### Demo Links
<ul>
    <li><a href="https://youtu.be/XMMmAgVsEFY">Video Demo</a></li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] A screen recording feature could be added to allow users to record their entire screen or a specific window while recording a video.
- [ ] Integration with Learning Management Systems (LMS): The application could be integrated with popular LMS platforms to streamline the classroom experience for both teachers and students.
- [ ] Video editing: A built-in video editor could be added to allow users to edit and enhance their recorded videos.
- [ ] Cloud storage: A cloud storage feature could be added to allow users to store their recorded videos securely and access them from anywhere.

See the [open issues](https://github.com/Yukino2002/Interacti/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Pratik Jallan - pratikjalan11@gmail.com

Project Link: [https://github.com/Yukino2002/Interacti](https://github.com/Yukino2002/Interacti)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [CVZone](https://github.com/cvzone/cvzone)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Davide Spalla](https://deepnote.com/@davidespalla/Recognizing-handwriting-with-Tensorflow-and-OpenCV-cfc4acf5-188e-4d3b-bdb5-a13aa463d2b0#00012-421d73cc-3b3a-4330-ab92-7e48462e68c3)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Yukino2002/Interacti.svg?style=for-the-badge
[contributors-url]: https://github.com/Yukino2002/Interacti/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Yukino2002/Interacti.svg?style=for-the-badge
[forks-url]: https://github.com/Yukino2002/Interacti/network/members
[stars-shield]: https://img.shields.io/github/stars/Yukino2002/Interacti.svg?style=for-the-badge
[stars-url]: https://github.com/Yukino2002/Interacti/stargazers
[issues-shield]: https://img.shields.io/github/issues/Yukino2002/Interacti.svg?style=for-the-badge
[issues-url]: https://github.com/Yukino2002/Interacti/issues
[license-shield]: https://img.shields.io/github/license/Yukino2002/Interacti.svg?style=for-the-badge
[license-url]: https://github.com/Yukino2002/Interacti/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/asimjawahir
[product-screenshot]: ./images/Interacti.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
