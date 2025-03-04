[comment]: <> (# MotionPriorCMax)

<h1 align="center"> MotionPriorCMax (中文注释版~仅供个人学习记录用)
</h1>

[comment]: <> ( <h2 align="center">PAPER</h2>)
  <h3 align="center">
  <a href="https://arxiv.org/pdf/2407.10802" target="_blank">Paper</a>
  | <a href="https://github.com/tub-rip/MotionPriorCMax" target="_blank">Original Github Page</a>
  | <a href="https://kwanwaipang.github.io/Awesome-Event-based-Contrast-Maximization/" target="_blank">Blog for CM</a>
  </h3>
  <div align="center"></div>

<!-- rm -rf .git -->

* 在dsec数据集上训练的代码
~~~
python scripts/flow_training.py --gpus 0 1 --config config/exe/flow_training/dsec.yaml
~~~