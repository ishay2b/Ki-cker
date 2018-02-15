import numpy as np
from datetime import datetime

from kicker.train import DataProvider
d = DataProvider()

from kicker.train import Trainer
from kicker import NeuralNet
nn = NeuralNet(24, (320, 480, 2))

t = Trainer(nn)

for j in range(5000):
    s = d.get_batch(sample=32)
    _, loss, diff = t.train_step(s)
    print(datetime.utcnow(), j, 'Loss ', loss, ' diff ', diff)

nn.save()