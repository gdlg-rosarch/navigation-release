# Script generated with Bloom
pkgdesc="ROS - This planner attempts to find a legal place to put a carrot for the robot to follow. It does this by moving back along the vector between the robot and the goal point."
url='http://wiki.ros.org/carrot_planner'

pkgname='ros-lunar-carrot-planner'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-lunar-base-local-planner'
'ros-lunar-catkin'
'ros-lunar-costmap-2d'
'ros-lunar-nav-core'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-tf'
)

depends=('eigen3'
'ros-lunar-base-local-planner'
'ros-lunar-costmap-2d'
'ros-lunar-nav-core'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-tf'
)

conflicts=()
replaces=()

_dir=carrot_planner
source=()
md5sums=()

prepare() {
    cp -R $startdir/carrot_planner $srcdir/carrot_planner
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

