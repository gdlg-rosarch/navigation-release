# Script generated with Bloom
pkgdesc="ROS - The move_base package provides an implementation of an action (see the <a href="http://www.ros.org/wiki/actionlib">actionlib</a> package) that, given a goal in the world, will attempt to reach it with a mobile base. The move_base node links together a global and local planner to accomplish its global navigation task. It supports any global planner adhering to the nav_core::BaseGlobalPlanner interface specified in the <a href="http://www.ros.org/wiki/nav_core">nav_core</a> package and any local planner adhering to the nav_core::BaseLocalPlanner interface specified in the <a href="http://www.ros.org/wiki/nav_core">nav_core</a> package. The move_base node also maintains two costmaps, one for the global planner, and one for a local planner (see the <a href="http://www.ros.org/wiki/costmap_2d">costmap_2d</a> package) that are used to accomplish navigation tasks."
url='http://wiki.ros.org/move_base'

pkgname='ros-lunar-move-base'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-base-local-planner'
'ros-lunar-catkin'
'ros-lunar-clear-costmap-recovery'
'ros-lunar-cmake-modules'
'ros-lunar-costmap-2d'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-message-generation'
'ros-lunar-move-base-msgs'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-navfn'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-rotate-recovery'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
)

depends=('ros-lunar-actionlib'
'ros-lunar-base-local-planner'
'ros-lunar-clear-costmap-recovery'
'ros-lunar-costmap-2d'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-message-runtime'
'ros-lunar-move-base-msgs'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-navfn'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-rotate-recovery'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
)

conflicts=()
replaces=()

_dir=move_base
source=()
md5sums=()

prepare() {
    cp -R $startdir/move_base $srcdir/move_base
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

