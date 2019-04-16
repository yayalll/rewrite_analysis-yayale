from .shufflenet_v2 import ShuffleNetV2

modeldict = {
    'analysis_shufflenetv2_bn': lambda inp, outp, size: ShuffleNetV2(inp, outp, size),
}
