# Run tests in check section
# Check is disabled by default because tests require Internet access
%bcond_with check

%global goipath         github.com/beevik/ntp
Version:                0.2.0

%global common_description %{expand:
The ntp package is an implementation of a Simple NTP (SNTP) client based on
RFC5905. It allows you to connect to a remote NTP server and request
information about the current time.}

%gometa

Name:           %{goname}
Release:        4%{?dist}
Summary:        A simple NTP client written in Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/ipv4)

# Test dependency
%if %{with check}
BuildRequires: golang(github.com/stretchr/testify)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
sed -i "s|\r||g" README.md


%install
%goinstall


%check
%if %{with check}
  %gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc RELEASE_NOTES.md README.md CONTRIBUTORS

%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-4
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.2.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Paul Gier <pgier@redhat.com> - 0.2.0-1
- First package for Fedora
