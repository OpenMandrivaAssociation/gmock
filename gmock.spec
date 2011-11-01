%define	major	0
%define libname	%mklibname	%{name} %{major}
%define develname	%mklibname	%{name} -d

Summary:        Google C++ Mocking Framework
Name:           gmock
Version:        1.6.0
Release:        1
License:        BSD
Group:          System/Libraries
URL:            http://code.google.com/p/googlemock/
Source0:        http://googlemock.googlecode.com/files/gmock-%{version}.zip
Patch0:			gmock-1.6.0-enable-install.patch
BuildRequires:  gtest-devel >= 1.6.0
BuildRequires:  python
Requires:	%{libname} = %{version}-%{release}

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
Summary:    Libraries for the %{name} package
Group:      System/Libraries

%description -n %{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--disable-static \
	--with-gtest \
	--enable-external-gtest

%make LIBS='-lpthread -lgtest'

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

# why repkg gtest
rm -fr %{buildroot}%{_includedir}/gtest/
rm -fr %{buildroot}%{_libdir}/libgtest*
rm -fr %{buildroot}%{_datadir}/aclocal

%check
%make check

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%doc CHANGES CONTRIBUTORS COPYING README
%{_libdir}/lib*.so
%{_includedir}/gmock/*

