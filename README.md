# Banana Navigation Project for Udacity DRLND

This project solves Banana navigation environment created with Unity.

## Environment Description

Agent can move in a field filled with yellow and blue bananas, restricted by walls. 

Action space is discrete, with 4 actions available:

 * `0` - move forward
 * `1` - move backward
 * `2` - turn left
 * `3` - turn right

Collecting a yellow banana yields `+1` reward while collecting blue banana gives `-1` reward.
Hence, the reward optimization goal is collecting as many yellow bananas as possible and avoiding as many blue bananas as possible.

Environment state is described with the vector of length `37` that contains agent's velocity (2) and ray-based perception of object 
around agent's forward direction (7 rays from different angles, each described as one-hot vector for 4 object categories, and the distance).

Environment is considered solved when the average reward over 100 episodes exceeds `13`.

## Getting Started

Following steps were tested for **Windows 10** with Anaconda installed. For other OS,
please refer to installation steps in the original [DLRND repo](https://github.com/udacity/deep-reinforcement-learning#dependencies).

1. Install [SWIG](https://sourceforge.net/projects/swig/files/swigwin/swigwin-4.0.1/swigwin-4.0.1.zip/download).
Unpack zip archive to any folder, open "Edit system environment variables", edit `Path` to add folder where `swig.exe` is located.

2. Create new Python environment in Anaconda prompt:
    ```
    conda create --name drlnd python=3.6
    activate drlnd
    conda install pytorch=0.4.0 -c pytorch
    ```

3. Checkout code and install dependencies:
    ```
    activate drlnd
    git clone https://github.com/vvmnnnkv/drlnd-navigation
    cd drlnd-navigation
    pip install -r requirements.txt
    python -m ipykernel install --user --name drlnd --display-name "drlnd"
    ```

4. Download the [Banana environment executable](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)  for Windows and unpack in the project folder.

5. Run jupyter notebook in the project root (this should open browser):
    ```
    jupyter notebook --notebook-dir=.
    ```

## Run Trained Agent
In jupyter, open `Navigation.ipynb` and follow instructions.


## Train Agent
In jupyter, open `Train.ipynb` and follow instructions.

