# Script generated with Bloom
pkgdesc="ROS - This package provides an implementation of a 2D costmap that takes in sensor data from the world, builds a 2D or 3D occupancy grid of the data (depending on whether a voxel based implementation is used), and inflates costs in a 2D costmap based on the occupancy grid and a user specified inflation radius. This package also provides support for map_server based initialization of a costmap, rolling window based costmaps, and parameter based subscription to and configuration of sensor topics."
url='http://wiki.ros.org/costmap_2d'

pkgname='ros-lunar-costmap-2d'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('pcl'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-laser-geometry'
'ros-lunar-map-msgs'
'ros-lunar-map-server'
'ros-lunar-message-filters'
'ros-lunar-message-generation'
'ros-lunar-nav-msgs'
'ros-lunar-pcl-conversions'
'ros-lunar-pcl-ros'
'ros-lunar-pluginlib'
'ros-lunar-rosbag'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-rosunit'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
'ros-lunar-voxel-grid'
)

depends=('pcl'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-laser-geometry'
'ros-lunar-map-msgs'
'ros-lunar-message-filters'
'ros-lunar-message-runtime'
'ros-lunar-nav-msgs'
'ros-lunar-pcl-conversions'
'ros-lunar-pcl-ros'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
'ros-lunar-voxel-grid'
)

conflicts=()
replaces=()

_dir=costmap_2d
source=()
md5sums=()

prepare() {
    cp -R $startdir/costmap_2d $srcdir/costmap_2d
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

