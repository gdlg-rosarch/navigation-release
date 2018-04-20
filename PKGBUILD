# Script generated with Bloom
pkgdesc="ROS - A path planner library and node."
url='http://wiki.ros.org/global_planner'

pkgname='ros-lunar-global-planner'
pkgver='1.15.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-angles'
'ros-lunar-catkin'
'ros-lunar-costmap-2d'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-navfn'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-tf'
)

depends=('ros-lunar-costmap-2d'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-navfn'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-tf'
)

conflicts=()
replaces=()

_dir=global_planner
source=()
md5sums=()

prepare() {
    cp -R $startdir/global_planner $srcdir/global_planner
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

