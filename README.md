

<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO
<br />
<div align="center">
  <a href="Paul_Bettany_as_Vision.jpg">
    <img src="Paul_Bettany_as_Vision.jpg" alt="Logo" width="120" height="120">
  </a>
-->
<h3 align="center">VISION</h3>

  <p align="center">
  This code is part of the iGEM UniLausanne 2021 project. 
A very basic image processing script initially used to measure AFP efficacy against frost damage on leaves. You can use it to calculate the ratio between two areas of given colors.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A very basic image processing script initially used to measure AFP efficacy against frost damage on leaves. You can use it to calculate the ratio between two areas of given colors.
We are not programmers so the code is somewhat blasphematory.
The code to find the best thresholds is in the Hsvthreshold.py file.
The code for the image processing is in the Vision.py file.
The HSV thresholder we used to define the thresholds comes from the following stackoverflow [thread](https://stackoverflow.com/questions/57282935/how-to-detect-area-of-pixels-with-the-same-color-using-opencv)
but any image editing software can be used to determine the threshold values.
<p align="right">(<a href="#top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

VISION is written in Python so, you must have an environment with all the necessary libraries for it to function.



* python libraries
  ```terminal
  pip install opencv2
  pip install csv
  pip install os
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/igemsoftware2021/UNILausanne-Vision
   ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


```python
1.Download the files
2.Install the necessary libraries in your python environment
3.open VISION.py with your code editor
4.replace input and output destinations
5.modify the prefix dictionnary according to your filenames
6.run
```
  
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

iGEM UNILausanne 2021 - [Website](https://2021.igem.org/Team:UNILausanne) - igem@unil.ch

Project Link: [https://github.com/igemsoftware2021/UNILausanne-Frozone](https://github.com/igemsoftware2021/UNILausanne-Frozone)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://ch.linkedin.com/in/igem-unil-1526621a3
[product-screenshot]: images/screenshot.png
