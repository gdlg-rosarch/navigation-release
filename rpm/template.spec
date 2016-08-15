Name:           ros-indigo-map-server
Version:        1.12.13
Release:        0%{?dist}
Summary:        ROS map_server package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/map_server
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL_image-devel
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rostest
Requires:       ros-indigo-tf
Requires:       yaml-cpp-devel
BuildRequires:  SDL_image-devel
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-tf
BuildRequires:  yaml-cpp-devel

%description
map_server provides the map_server ROS Node, which offers map data as a ROS
Service. It also provides the map_saver command-line utility, which allows
dynamically generated maps to be saved to file.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 15 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.13-0
- Autogenerated by Bloom

* Fri Jun 24 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.12-0
- Autogenerated by Bloom

* Wed Jun 08 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.11-0
- Autogenerated by Bloom

* Fri May 27 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.10-0
- Autogenerated by Bloom

* Thu May 26 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.9-0
- Autogenerated by Bloom

* Mon May 16 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.8-0
- Autogenerated by Bloom

* Sat Feb 06 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.7-0
- Autogenerated by Bloom

* Sat Jan 02 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.6-0
- Autogenerated by Bloom

* Fri Oct 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.5-0
- Autogenerated by Bloom

* Wed Jun 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.4-0
- Autogenerated by Bloom

* Thu Apr 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.3-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.2-0
- Autogenerated by Bloom

* Sat Mar 14 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Wed Feb 04 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

