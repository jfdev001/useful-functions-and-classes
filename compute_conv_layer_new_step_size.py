def compute_conv_layer_new_step_size(self, input_size, kernel_size, padding=0, stride=1):
        """Calculates '?' in (n, ?, filters) from convolutional layers.

        From https://dingyan89.medium.com/calculating-parameters-of-convolutional-and-fully-connected-layers-with-keras-186590df36c6

        :param input_size: <class 'int'> For an image set (n, 32, 32, 3), 
            timesteps would be 32. It is just the second dimension of
            any batch input tensor.
        :param kernel_size: <class 'int'>
        :param padding: <class 'int'>
        :param stride: <class 'int'>
        """

        return int(((input_size - kernel_size + 2 * padding)/(stride)) + 1)
