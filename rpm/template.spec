Name:           ros-kinetic-robot-pose-ekf
Version:        1.14.3
Release:        0%{?dist}
Summary:        ROS robot_pose_ekf package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robot_pose_ekf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-bfl
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-bfl
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-rosbag
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
The Robot Pose EKF package is used to estimate the 3D pose of a robot, based on
(partial) pose measurements coming from different sources. It uses an extended
Kalman filter with a 6D model (3D position and 3D orientation) to combine
measurements from wheel odometry, IMU sensor and visual odometry. The basic idea
is to offer loosely coupled integration with different sensors, where sensor
signals are received as ROS messages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Mar 16 2018 David V. Lu!! <davidvlu@gmail.com> - 1.14.3-0
- Autogenerated by Bloom

* Mon Aug 14 2017 David V. Lu!! <davidvlu@gmail.com> - 1.14.2-0
- Autogenerated by Bloom

* Mon Aug 07 2017 David V. Lu!! <davidvlu@gmail.com> - 1.14.1-0
- Autogenerated by Bloom

* Fri May 20 2016 David V. Lu!! <davidvlu@gmail.com> - 1.14.0-0
- Autogenerated by Bloom

