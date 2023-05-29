import tensorflow as tf
from transunet import TransUNet

def get_model(weigths_path):
    model = TransUNet(
        image_size = 224, 
        pretrain = True,
        num_classes = 12+1,
        final_act = 'softmax',
        freeze_enc_cnn=False,
    )
    model.load_weights(weigths_path)
    return model