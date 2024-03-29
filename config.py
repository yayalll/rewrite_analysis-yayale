from easydict import EasyDict

configer = EasyDict()


configer.dsize = (64, 64)
configer.n_channel = 1
configer.n_class = 63


configer.splitmode = 'split_{}x{}_1'.format(configer.dsize[0], configer.dsize[1])
configer.modelbase = 'analysis_shufflenetv2_bn'

configer.modelname = '{}_{}'.\
                    format(configer.modelbase, configer.splitmode)


configer.datapath = '/datasets/ECUST2019_{}x{}'.\
                                format(configer.dsize[0], configer.dsize[1])
configer.logspath = './logs/{}_{}subjects_logs'.format(configer.modelname, configer.n_class)
configer.mdlspath = './modelfiles/{}_{}subjects_models'.format(configer.modelname, configer.n_class)


## training step
configer.batchsize = 128
configer.n_epoch   = 35

## learing rate
configer.lrbase = 0.001
configer.stepsize = 20
configer.gamma = 0.1

configer.cuda = True
