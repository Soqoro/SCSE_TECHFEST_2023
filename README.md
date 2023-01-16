# :parking: SimpliPark 

## :family_man_woman_boy_boy: Team 51 
Team Member Names:
1. Sua Qi Rong
2. Tan Yue Yang Kane
3. Chong Wei Kang
4. Fong Ye Xuan

## :writing_hand: Overview
Our team aims to develop a web application targeted towards the general public in improving their experience at finding available carpark lots. The application utilises computer vision in identifying empty carpark lots and outputs the real time information on the website for the general public.

## 🔎 Identified Problem
HDB manages over 2000 car parks, with more than 660k car parks and 7000 equipment that supports the operations of the car park. Our car parks are visited by 500k unique motorists and the system processes 2.5m transactions daily. It is not possible for HDB to deploy staff/maintenance teams to every car park, due to the sheer number of car parks and equipment. Also, the situation is exacerbated by the manpower crunch brought about by our ageing population. 
For drivers, they face many problems finding empty parking spaces with drivers needing to drive around aimlessly in hopes of finding a carpark with empty lots.
Hence, we are looking for a solution that allows HDB to rely on the residents to take ownership of their estate’s well-being, and for drivers to more easily find car park with empty lots.

## 🚀 Features
### 1. Display empty carpark lots
The web application allows users to choose their desired car park, or to detect the car parks nearest to them using their location. Then, a live feed of the car park is displayed, with the number of empty lots and the capacity of the car park. This allows users to make better decisions as to which car park they should go, saving time and fuel.
### 2. User reporting system
Through observing the live feed, users are able to report problems for the specific selected car parks. This can facilitate timely maintenance of car parks without requiring heavy deployment of staff/maintenance teams, encouraging residents to take ownership of their estate’s well-being.

## :keyboard: Specifications
### 1. Computer Vision (CV)
Usage of Python open source CV librariesto detect empty parking lots in car parks. This image will also be shown on the website as a live feed for users to monitor.

### 2. Front-end web development
HTML, BootStrap, CSS, JavaScript to build the web app and display all car parks around the area.

## 💡 Limitations
### 1. Night model
The program written for the computer vision algorithm is calibrated for day time usage by installing image sensors in car parks. If the brightness level at night is too dark, infrared sensors may be required to augment the computer vision system to continue ensuring high accuracy for the information provided on the website.
### 2. Multi-storeyed structure of HDB car parks
Our prototype is created using an overhead view of open-air car parks, where one image is able to capture hundreds of parking lots. In HDB carparks where they are usually multi-storeyed, it will be difficult to capture many parking lots in one image. Therefore, many cameras would be required, increasing cost. Overview
Our team aims to develop a web application targeted towards the general public in improving their experience at finding available carpark lots. The application utilises computer vision in identifying empty carpark lots and outputs the real time information on the website for the general public.

# 🧑🏽‍🤝‍🧑🏽 Contributors
* [Chong Wei Kang](https://github.com/weikangg)
* [Ken Fong Ye Xuan](https://github.com/kenfyxx)
* [Sua Qi Rong](https://github.com/Soqoro)
* [Kane Tan Yue Yang](https://github.com/kanetan4)
