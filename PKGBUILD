# Script generated with Bloom
pkgdesc="ROS - This package provides implementations of the Trajectory Rollout and Dynamic Window approaches to local robot navigation on a plane. Given a plan to follow and a costmap, the controller produces velocity commands to send to a mobile base. This package supports both holonomic and non-holonomic robots, any robot footprint that can be represented as a convex polygon or circle, and exposes its configuration as ROS parameters that can be set in a launch file. This package's ROS wrapper adheres to the BaseLocalPlanner interface specified in the <a href="http://wiki.ros.org/nav_core">nav_core</a> package."
url='http://wiki.ros.org/base_local_planner'

pkgname='ros-lunar-base-local-planner'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'pcl'
'ros-lunar-angles'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-cmake-modules'
'ros-lunar-costmap-2d'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-message-generation'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-pcl-conversions'
'ros-lunar-pcl-ros'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-rosunit'
'ros-lunar-std-msgs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
'ros-lunar-voxel-grid'
)

depends=('eigen3'
'pcl'
'ros-lunar-angles'
'ros-lunar-costmap-2d'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-message-runtime'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-pcl-ros'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-std-msgs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
'ros-lunar-voxel-grid'
)

conflicts=()
replaces=()

_dir=base_local_planner
source=()
md5sums=()

prepare() {
    cp -R $startdir/base_local_planner $srcdir/base_local_planner
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

