# Script generated with Bloom
pkgdesc="ROS - A 2D navigation stack that takes in information from odometry, sensor streams, and a goal pose and outputs safe velocity commands that are sent to a mobile base."
url='http://wiki.ros.org/navigation'

pkgname='ros-kinetic-navigation'
pkgver='1.14.3_1'
pkgrel=1
arch=('any')
license=('BSD,LGPL,LGPL (amcl)'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-amcl'
'ros-kinetic-base-local-planner'
'ros-kinetic-carrot-planner'
'ros-kinetic-clear-costmap-recovery'
'ros-kinetic-costmap-2d'
'ros-kinetic-dwa-local-planner'
'ros-kinetic-fake-localization'
'ros-kinetic-global-planner'
'ros-kinetic-map-server'
'ros-kinetic-move-base'
'ros-kinetic-move-base-msgs'
'ros-kinetic-move-slow-and-clear'
'ros-kinetic-nav-core'
'ros-kinetic-navfn'
'ros-kinetic-robot-pose-ekf'
'ros-kinetic-rotate-recovery'
'ros-kinetic-voxel-grid'
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

