from .base import TrajectoryLossBase
from .focus import FocusLoss


class LossFactory:
    @staticmethod
    def get_loss_calculator(loss_name, loss_config, profiler=None):
        if loss_name == 'FOCUS':
            return FocusLoss(**loss_config, profiler=profiler)#返回一个FocusLoss的实例
        else:
            raise ValueError("Unsupported loss type")
