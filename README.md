# Collision Detection Neural Net

Neural network made to predict the best path for a robot to take to avoid collison.

The project might work with different versions of python but the one I've tested is Python 3.11.5


To run the current model locally:

1. Clone the project 
2. Run `pip install -r requirements.txt`
3. Run `python goal_seeking.py`


To update the model after making adjustments to how its trained:

1. Make changes to `train_model.py`
2. Run `python train_model.py`
3. Then rerun `python goal_seeking.py` to see how the new training impacts performance


To collect different kinds of data:

1. Make changes to `collect_data.py`
2. Then run `python collect_data.py` to generate a new training_data.csv

Demo video of the current status of the project ![here](/assets/demo.gif)
