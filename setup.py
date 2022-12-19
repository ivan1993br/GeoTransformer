from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


setup(
    name='geotransformer',
    version='1.0.0',
    packages=['geotransformer/datasets',
              'geotransformer/datasets/registration',
              'geotransformer/datasets/registration/kitti',
              'geotransformer/datasets/registration/modelnet',
              'geotransformer/datasets/registration/threedmatch',
              'geotransformer/engine',
              'geotransformer/modules',
              'geotransformer/modules/geotransformer',
              'geotransformer/modules/kpconv',
              'geotransformer/modules/layers',
              'geotransformer/modules/loss',
              'geotransformer/modules/loss',
              'geotransformer/modules/ops',
              'geotransformer/modules/registration',
              'geotransformer/modules/sinkhorn',
              'geotransformer/modules/transformer',
              'geotransformer/transforms',
              'geotransformer/utils'],
    scripts=['geotransformer/scripts/geotransformer_ply_io'],
    ext_modules=[
        CUDAExtension(
            name='geotransformer.ext',
            sources=[
                'geotransformer/extensions/extra/cloud/cloud.cpp',
                'geotransformer/extensions/cpu/grid_subsampling/grid_subsampling.cpp',
                'geotransformer/extensions/cpu/grid_subsampling/grid_subsampling_cpu.cpp',
                'geotransformer/extensions/cpu/radius_neighbors/radius_neighbors.cpp',
                'geotransformer/extensions/cpu/radius_neighbors/radius_neighbors_cpu.cpp',
                'geotransformer/extensions/pybind.cpp',
            ],
        ),
    ],
    cmdclass={'build_ext': BuildExtension},
)
