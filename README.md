# garden
A simple NLP exercise

## Table of Contents

1. Overview of the Project
2. Installing and Running the Project
3. Usage of the Project
4. Credits

### Overview of the Project

This project was written as part of the HyperionDev University of Edinburgh Online Software Engineering Bootcamp, to demonstrate and practice the use of basic NLP concepts using SpaCy in Python.

### Installing and Running the Project

The project was written in Python 3.11.0 using the Visual Studio Code IDE version 1.75.0.  You will require Python 3 to run this project in your IDE.

There is a Dockerfile attached which allows you to complile and run this on any machine; the Dockerfile uses Python 3.7, as I have found this gives the quickest results creating a Docker container and image with SpaCy.  Note there is no requirements.txt file, as the Dockerfile itself contains the instructions for installing SpaCy and the relevant language model.

This project can also be found on Docker Hub at: https://hub.docker.com/repository/docker/jjhughes1969/garden/general

### Usage of the Project

The project requires no user input and can be run in an IDE or Console.

It analyses five "garden path" sentences, provided in a list as follows:

![Screenshot 2023-02-10 at 10 23 26](https://user-images.githubusercontent.com/124285490/218068199-3ef8da3f-57d3-496a-9da4-c9e5fd78dba0.png)

It tokenises those sentences and produces the following output:

![Screenshot 2023-02-10 at 10 24 03](https://user-images.githubusercontent.com/124285490/218068712-d1a08bb0-1ad5-431b-a1f2-3ba390e3d170.png)

It also performs entity analysis on the sentences and produces the following output:

![Screenshot 2023-02-10 at 10 24 13](https://user-images.githubusercontent.com/124285490/218068739-b82df7e1-a65c-4a06-b6b2-16381eb5a386.png)

Finally, the code contains comments on two of the entitites as follows:

![Screenshot 2023-02-10 at 10 24 27](https://user-images.githubusercontent.com/124285490/218068772-c1e6b79f-f737-47aa-9ad5-d007fb5d1523.png)

### Credits

The Python code was written by Jonathan Hughes, based on materials and instructions provided by HyperionDev.
The HyperionDev website is at https://www.hyperiondev.com
