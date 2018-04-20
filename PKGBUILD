# Script generated with Bloom
pkgdesc="ROS - This package provides a recovery behavior for the navigation stack that attempts to clear space by performing a 360 degree rotation of the robot."
url='http://wiki.ros.org/rotate_recovery'

pkgname='ros-lunar-rotate-recovery'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-lunar-base-local-planner'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-costmap-2d'
'ros-lunar-nav-core'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-tf'
)

depends=('eigen3'
'ros-lunar-costmap-2d'
'ros-lunar-nav-core'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-tf'
)

conflicts=()
replaces=()

_dir=rotate_recovery
source=()
md5sums=()

prepare() {
    cp -R $startdir/rotate_recovery $srcdir/rotate_recovery
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

