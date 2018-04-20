# Script generated with Bloom
pkgdesc="ROS - voxel_grid provides an implementation of an efficient 3D voxel grid. The occupancy grid can support 3 different representations for the state of a cell: marked, free, or unknown. Due to the underlying implementation relying on bitwise and and or integer operations, the voxel grid only supports 16 different levels per voxel column. However, this limitation yields raytracing and cell marking performance in the grid comparable to standard 2D structures making it quite fast compared to most 3D structures."
url='http://wiki.ros.org/voxel_grid'

pkgname='ros-kinetic-voxel-grid'
pkgver='1.14.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin>=0.5.68'
'ros-kinetic-roscpp'
'ros-kinetic-rosunit'
)

depends=('ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=voxel_grid
source=()
md5sums=()

prepare() {
    cp -R $startdir/voxel_grid $srcdir/voxel_grid
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

