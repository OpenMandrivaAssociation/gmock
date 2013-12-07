%define	major	0
%define libname	%mklibname %{name} %{major}
%define libmain	%mklibname %{name}_main %{major}
%define devname	%mklibname %{name} -d

Summary:	Google C++ Mocking Framework
Name:		gmock
Version:	1.6.0
Release:	6
License:	BSD
Group:		System/Libraries
Url:		http://code.google.com/p/googlemock/
Source0:	http://googlemock.googlecode.com/files/gmock-%{version}.zip
Patch0:		gmock-1.6.0-enable-install.patch
BuildRequires:	gtest-devel >= 1.6.0
BuildRequires:	python

%description
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s
specifics in mind, Google C++ Mocking Framework (or Google Mock for
short) is a library for writing and using C++ mock classes.

Google Mock:

 o lets you create mock classes trivially using simple macros,
 o supports a rich set of matchers and actions,
 o handles unordered, partially ordered, or completely ordered
   expectations,
 o is extensible by users, and
 o works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and
   Symbian.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Library for %{name}.

%package -n %{libmain}
Summary:	Libraries for the %{name} package
Group:		System/Libraries
Conflicts:	%{_lib}gmock0 < 1.6.0-2

%description -n %{libmain}
Library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libmain} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--with-gtest \
	--enable-external-gtest

%make LIBS='-lpthread -lgtest'

%install
%makeinstall_std

# why repkg gtest
rm -fr %{buildroot}%{_includedir}/gtest/
rm -fr %{buildroot}%{_libdir}/libgtest*
rm -fr %{buildroot}%{_datadir}/aclocal

%check
%make check

%files -n %{libname}
%{_libdir}/libgmock.so.%{major}*

%files -n %{libmain}
%{_libdir}/libgmock_main.so.%{major}*

%files -n %{devname}
%doc CHANGES CONTRIBUTORS COPYING README
%{_libdir}/lib*.so
%{_includedir}/gmock/*

