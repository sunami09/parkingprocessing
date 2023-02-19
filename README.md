<div align="center">
<h1>Spottr</h1>
<img src="https://cdn.shopify.com/s/files/1/0625/9133/6672/files/1fdcb7_f4f55cd25f834008910ca0d3f7265a11_mv2_1024x1024.gif?v=1661782308" width ="400">
<p>Navigate with ease, locate open spots quickly, and get notified about busy lots. Find parking stress-free, save time, and reduce carbon emissions with our parking lot tracker. Join us in creating a greener future, one parking spot at a time.</p>
</div>

## How to run it

```bash
git clone https://github.com/sunami09/parkingprocessing.git
pip3 install -r dependencies.txt
python3 main_.py
```
<!---
<div align="center">
  <img src ="" width ="">
</div>
-->
 

## Walkthrough
- **Starting Page**
  - The program starts and a pop-up window appears.
  
  <br>
  
  <div align="center">
  <img src ="https://user-images.githubusercontent.com/66564001/219957899-cf8a1ee8-694d-4156-bcd4-43f106667989.png" width ="600">
 </div>
 
- **Learn More**
  - It gives you a brief description of what Spottr does.
  
  <br>

   <div align="center">
  <img src ="https://user-images.githubusercontent.com/66564001/219958171-8429df7c-6579-4717-96f8-e6a40b912750.png" width ="600">
</div>

- **Try Out!**
  - It gives you option to select from:
  
  <br>
  
  <div align="center">
  <img src ="https://user-images.githubusercontent.com/66564001/219958470-1f8d5980-3fc9-4003-9a2f-b749a9372981.gif" width ="600">
</div>

- **Parking Spot Detection**
  - It detects all the spot that are available and marks them as green while others red.
  
  <br>
  
  <div align="center">
  <img src ="https://user-images.githubusercontent.com/66564001/219959554-f21380d8-f719-4f35-abab-ab6ead1ef1bf.gif" width ="700">
</div>
  
 ## How we built it
- ### Data Collection
  - Our system requires video footage of parking lots from a top/bird's-eye view.
  - We conducted an internet search to find the necessary videos for our project.
- ### Reading The Videos
  - We utilized the OpenCV library to read, write, and display the videos.
  - We created two Python files, 'ParkingSpaceMarker.py' and 'main.py'.
- ### Area of Interest(ParkingSpaceMaker.py)
  - As running a for-loop was inconvenient due to irregular spacing in the parking lots, we manually marked the spots using rectangular boxes.
  - We then stored these coordinates in a binary file for 'main.py' to utilize and mark the spots on the video.
- ### Image Processing(Main.py)
  - We read the binary file and marked the parking spots as empty or occupied on the video.
  - To increase focus and reduce distractions, we converted the RGB image to grayscale.
  - We applied Gaussian blur to reduce visual noise such as shadows and reflections and to detect the edges of the parking spots more accurately.
  - We then used adaptive thresholding to segment the foreground and background and create a binary image based on pixel intensity due to poor lighting conditions in the footage.
  - We applied median blur to further smooth the image and reduce salt-and-pepper noise.
  - We used dilation to fill small gaps and reduce the risk of false negatives.
  - Finally, we counted the number of non-zero pixels in the binary image to determine which parking spots were occupied or available.
- ### User Experience
  - We utilized the tkinter library to create a more user-friendly interface instead of command-line interaction.
## Authors
- [Sunami Dasgupta](https://github.com/sunami09)
- [Alessandro Sisniegas](https://github.com/alessandrosisniegas)
