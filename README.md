# Python OpenCV

This project is intended to be a simple reference or guide for using OpenCV with Python, along with some Unit Tests from Test Driven Development. All this inside a Docker container.

#### Resources
In case  you want to know more about any of these:
| Topic | Documentation |
| ------ | ------ |
| Python 3 | https://docs.python.org/3.7/ |
| Open CV | https://docs.opencv.org/4.2.0/ |
| Unit Testing | https://docs.python.org/3/library/unittest.html |
| Docker | https://docs.docker.com/ |

## Docker Commands
#### Build
Here, I am assuming that you kept the file name as python-opencv and that you want to tag the Docker image as python-opencv, but you are free to name them as you wish.
This will create the Docker image we will use later for creating our container:
```sh
cd python-opencv
docker build -t python-opencv .
```
#### Run
This will have the Docker container running:
```sh
docker run -it -v "$(pwd)":/usr/src/python-opencv python-opencv
```
Or:
```sh
docker run -it --mount type=bind,source="$(pwd)",destination=/usr/src/python-opencv,consistency=cached python-opencv
```
Here I had a couple **difficulties** because I'm using **Docker on Windows 10 Home**, and Docker was complaining about the **specified path**, wich I solved as follows:

  1. Go to Oracle VM VirtualBox
  2. Right click on default vm
  3. Go to Settings - Shared Folders
  4. Add your folder as Permanent and Auto-mount
  
- Once you've done this, instead of using ```"$(pwd)"``` use your folder:
  - ```-v //my_folder/my_project:/usr/src/python-opencv```
  - ```source=//my_folder/my_project,destination=/usr/src/python-opencv```

***This is Work In Progress, so the next steps are adding some Python code using OpenCV and some Tests.***