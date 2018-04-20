# Script generated with Bloom
pkgdesc="ROS - move_slow_and_clear"
url='http://wiki.ros.org/move_slow_and_clear'

pkgname='ros-kinetic-move-slow-and-clear'
pkgver='1.14.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-costmap-2d'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nav-core'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-costmap-2d'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nav-core'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=move_slow_and_clear
source=()
md5sums=()

prepare() {
    cp -R $startdir/move_slow_and_clear $srcdir/move_slow_and_clear
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

