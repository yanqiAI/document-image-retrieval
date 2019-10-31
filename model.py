# coding:utf-8
from keras.layers import Input, Dense, Lambda
from keras import backend as K
from keras.callbacks import Callback
from keras.applications.densenet import DenseNet121
from keras_efficientnets import EfficientNetB4
from keras.constraints import unit_norm
from keras.models import Model
from IPython.core.debugger import Tracer

class UpdateAnnealingParameter(Callback):
    def __init__(self, gamma, nb_epochs, verbose=0):
        super(UpdateAnnealingParameter, self).__init__()
        self.gamma = gamma
        self.nb_epochs = nb_epochs
        self.verbose = verbose

    def on_epoch_begin(self, epoch, logs=None):
        new_gamma = 2.0 * (self.nb_epochs - epoch) / self.nb_epochs
        K.set_value(self.gamma, new_gamma)

        if self.verbose > 0:
            print('\nEpoch %05d: UpdateAnnealingParameter reducing gamma to %s.' % (epoch + 1, new_gamma))


# EfficientNet network
def efficientnet_B4(input_channel_num = 1):
    input_layer = Input(shape = (380, 380, input_channel_num))
    dense = EfficientNetB4(include_top = False, weights = None, input_tensor = input_layer, pooling = 'max')
    x = dense.output
    x = Dense(2048, activation = 'tanh')(x)

    # normolize weights and features, then classification
    encoder = Lambda(lambda m: K.l2_normalize(m, axis=1))(x)
    x = Dense(1500, use_bias = False, kernel_constraint = unit_norm())(encoder)

    # build a model and return
    model = Model(inputs = input_layer, outputs = x)

    return model


if __name__ == '__main__':
    model = efficientnet_B4()
    # model.summary()
    base_model = Model(inputs = model.input, outputs = model.get_layer('dense_1').output)
    base_model.summary()
