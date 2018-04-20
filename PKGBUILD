# Script generated with Bloom
pkgdesc="ROS - navfn provides a fast interpolated navigation function that can be used to create plans for a mobile base. The planner assumes a circular robot and operates on a costmap to find a minimum cost plan from a start point to an end point in a grid. The navigation function is computed with Dijkstra's algorithm, but support for an A* heuristic may also be added in the near future. navfn also provides a ROS wrapper for the navfn planner that adheres to the nav_core::BaseGlobalPlanner interface specified in <a href="http://wiki.ros.org/nav_core">nav_core</a>."
url='http://wiki.ros.org/navfn'

pkgname='ros-lunar-navfn'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('netpbm'
'pcl'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-cmake-modules'
'ros-lunar-costmap-2d'
'ros-lunar-geometry-msgs'
'ros-lunar-message-generation'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-pcl-conversions'
'ros-lunar-pcl-ros'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rosunit'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
)

depends=('pcl'
'ros-lunar-costmap-2d'
'ros-lunar-geometry-msgs'
'ros-lunar-message-runtime'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-pcl-conversions'
'ros-lunar-pcl-ros'
'ros-lunar-pluginlib'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-tf'
'ros-lunar-visualization-msgs'
)

conflicts=()
replaces=()

_dir=navfn
source=()
md5sums=()

prepare() {
    cp -R $startdir/navfn $srcdir/navfn
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

