# -*- coding: utf-8 -*-
"""feature_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V_0n7FmQRYQ8TdK8eVmgfk2kqg88Xd1W
"""

import torch

with torch.no_grad():
    model = CNN()
    model.load_state_dict(torch.load('/content/drive/My Drive/SML _ PROJECT/CASIA_2_patchs.pt',
                                     map_location=lambda storage, loc: storage))
    model.eval()
    model = model.double()
    model

import pandas as pd
import numpy as np
import glob
import cv2
from skimage.util import view_as_windows

from tqdm import tqdm

create_feature_vectors(model)

train_au =pd.read_csv('auth_train_new.csv')
test_au=pd.read_csv('authentic_test_new.csv')

train_tp=pd.read_csv('au_test_c1.csv')
test_tp=pd.read_csv('tp_test_c1.csv')

create_feature_vectors(model)

newdf=pd.concat([train_au,train_tp])

train_au.insert(1, 'label', '1')

train_au

train_tp.insert(1, 'label', '0')

newdf.to_csv('train.csv')

# flag true means this is tha tampered dataset and flag false means it is authentic dataset
def create_features(paths,flag,model):
  if flag == True:
    lables = np.ones(len(paths))
  else:
    lables = np.zeros(len(paths))
  y = pd.DataFrame()
  y['images'] = paths
  y['Label'] = lables
  feature_vector = {}
  for i in paths:
    im = io.imread(i)
    feature_vector[i] = fetch_model(im,model)
  x = pd.DataFrame()

  # x.iloc[0] = list(fe.values())[0]
  # x['image'] = list(fe.keys())[0]
  for i in feature_vector.values():
    x = x.append(list(i), ignore_index=True)
    # x= x.append(list(fe.values())[1], ignore_index=True)
    # x= x.append(list(fe.values())[2], ignore_index=True)
  
  
  
  return pd.concat([y,x],axis=1)

def fetch_model(mat,model):
  transform = transforms.Compose([transforms.ToTensor()])
  vector = []
  patches = create_patches(mat,128)
  for i in patches:
    img_tensor = transform(i)
    img_tensor.unsqueeze_(0)
    img_variable = Variable(img_tensor.double())
    yi = get_yi(model=model,patch=img_variable).tolist()
    vector.append(yi)
  
  return list(np.mean(vector,axis=0))

y = [[1,2,3],[4,5,6]]

y = np.asarray(y)

list(np.mean(y, axis = 0))

def create_patches(mat,stride):
  window_shape = (128, 128, 3)
  # print(image_mat.shape)
  
  windows = view_as_windows(mat, window_shape, step=stride)
  patches = []
  for m in range(windows.shape[0]):
      for n in range(windows.shape[1]):
          patches.append(windows[m][n][0])
  return patches

import torch
model = CNN()
model.load_state_dict(torch.load('/content/drive/My Drive/SML _ PROJECT/CASIA2_NoRot_LR0001_b200_nodrop.pt',
                                  map_location=lambda storage, loc: storage))

import pandas as pd
train_au =list(pd.read_csv('authentic_test_new.csv')['0'])

len(train_au)

train_auth = create_features(train_au,False,model)

len(train_auth)

train_tp =list(pd.read_csv('tampered_test_new.csv')['0'])

train_tamp = create_features(train_tp,True,model)

len(train_tamp)

pd.concat([train_auth,train_tamp]).to_csv('/content/drive/My Drive/SML _ PROJECT/bhakti_test',index=False)

x = pd.DataFrame()

# x.iloc[0] = list(fe.values())[0]
# x['image'] = list(fe.keys())[0]
x = x.append(list(fe.values())[0], ignore_index=True)
x= x.append(list(fe.values())[1], ignore_index=True)
x= x.append(list(fe.values())[2], ignore_index=True)

y = pd.DataFrame()
y['images'] = fe.keys()
y['Label'] = la

pd.concat([y,x],axis=1)

train_tp=list(pd.read_csv('tampered_train_new.csv')['0'])

fe,la = create_features(train_tp[0:3],True,model)
x = pd.DataFrame()

# x.iloc[0] = list(fe.values())[0]
# x['image'] = list(fe.keys())[0]
x = x.append(list(fe.values())[0], ignore_index=True)
x= x.append(list(fe.values())[1], ignore_index=True)
x= x.append(list(fe.values())[2], ignore_index=True)
y = pd.DataFrame()
y['images'] = fe.keys()
y['Label'] = la
pd.concat([y,x],axis=1)

from skimage import io
import cv2

model.eval()

im = io.imread(train_au[0])

patches = create_patches(im,128)

p = get_patches(im,128)

len(patches)

len(p)

patches[0].shape

p[0].shape

patches[0][0].shape

transform = transforms.Compose([transforms.ToTensor()])



# patches = get_patches(image, stride=128)

for patch in p:  # for every patch
    img_tensor = transform(patch)
    img_tensor.unsqueeze_(0)
    img_variable = Variable(img_tensor.double())
    yi = get_yi(model=model, patch=img_variable)

yi.tolist()

p = ['CASIA2/Au/Au_ani_30120.jpg', 'CASIA2/Au/Au_pla_30030.jpg',
       'CASIA2/Au/Au_nat_30649.jpg', ...,
       'CASIA2/Tp/Tp_S_CNN_S_N_pla00024_pla00024_00561.tif',
       'CASIA2/Tp/Tp_D_NRN_S_N_sec00100_ani00005_00708.tif',
       'CASIA2/Tp/Tp_S_NNN_S_N_sec20009_sec20009_01444.tif']



"""#analysis on misclassification"""

from skimage import io

io.imshow(io.imread('CASIA2/Au/Au_nat_00084.jpg'))

io.imshow(io.imread('CASIA2/Tp/Tp_D_CRN_M_N_nat00084_nat00086_10073.tif'))

io.imshow(io.imread('CASIA2/Au/Au_pla_10114.jpg'))

io.imshow(io.imread('CASIA2/Tp/Tp_D_CNN_S_N_pla10114_ani00081_10429.tif'))

io.imshow(io.imread('CASIA2/Tp/Tp_S_NNN_S_N_art20035_art20035_01841.tif'))

io.imshow(io.imread('CASIA2/Au/Au_art_20035.jpg'))

io.imshow(io.imread('CASIA2/Au/Au_pla_20080.jpg'))

io.imshow(io.imread(p[1]))

io.imshow(io.imread(p[2]))

io.imshow(io.imread(p[3]))

p[3]

