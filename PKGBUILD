# Script generated with Bloom
pkgdesc="ROS - A 2D navigation stack that takes in information from odometry, sensor streams, and a goal pose and outputs safe velocity commands that are sent to a mobile base."
url='http://wiki.ros.org/navigation'

pkgname='ros-lunar-navigation'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD,LGPL,LGPL (amcl)'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-amcl'
'ros-lunar-base-local-planner'
'ros-lunar-carrot-planner'
'ros-lunar-clear-costmap-recovery'
'ros-lunar-costmap-2d'
'ros-lunar-dwa-local-planner'
'ros-lunar-fake-localization'
'ros-lunar-global-planner'
'ros-lunar-map-server'
'ros-lunar-move-base'
'ros-lunar-move-base-msgs'
'ros-lunar-move-slow-and-clear'
'ros-lunar-nav-core'
'ros-lunar-navfn'
'ros-lunar-robot-pose-ekf'
'ros-lunar-rotate-recovery'
'ros-lunar-voxel-grid'
)

conflicts=()
replaces=()

_dir=navigation
source=()
md5sums=()

prepare() {
    cp -R $startdir/navigation $srcdir/navigation
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

