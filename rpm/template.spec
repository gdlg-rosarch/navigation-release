Name:           ros-hydro-costmap-2d
Version:        1.11.15
Release:        0%{?dist}
Summary:        ROS costmap_2d package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/costmap_2d
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-laser-geometry
Requires:       ros-hydro-map-msgs
Requires:       ros-hydro-message-filters
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-pcl-conversions
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rostest
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
Requires:       ros-hydro-voxel-grid
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-laser-geometry
BuildRequires:  ros-hydro-map-msgs
BuildRequires:  ros-hydro-map-server
BuildRequires:  ros-hydro-message-filters
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-rosbag
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-voxel-grid

%description
This package provides an implementation of a 2D costmap that takes in sensor
data from the world, builds a 2D or 3D occupancy grid of the data (depending on
whether a voxel based implementation is used), and inflates costs in a 2D
costmap based on the occupancy grid and a user specified inflation radius. This
package also provides support for map_server based initialization of a costmap,
rolling window based costmaps, and parameter based subscription to and
configuration of sensor topics.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Feb 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.15-0
- Autogenerated by Bloom

* Fri Dec 05 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

