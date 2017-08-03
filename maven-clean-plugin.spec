%{?scl:%scl_package maven-clean-plugin}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-clean-plugin
Version:        3.0.0
Release:        3.2%{?dist}
Summary:        Maven Clean Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-clean-plugin/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-compat)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-utils)

%description
The Maven Clean Plugin is a plugin that removes files generated 
at build-time in a project's directory.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -n %{pkg_name}-%{version} -q 

# junit dependency was removed in Plexus 1.6
%pom_add_dep junit:junit::test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 3.0.0-3.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.0.0-3.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.1-2
- Add test dependency on junit

* Tue Oct 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6.1-1
- Update to upstream version 2.6.1

* Fri Sep 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6
- Enable tests
- Remove Obsoletes/Provides for maven2-plugin-clean

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-10
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-8
- Use Requires: java-headless rebuild (#1067528)

* Tue Aug 06 2013 Michal Srb <msrb@redhat.com> - 2.5-7
- Adapt to current guidelines
- Install LICENSE+NOTICE file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-5
- Add maven-core to test dependencies
- Resolves: rhbz#914165

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.5-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Alexander Kurtakov <akurtako@redhat.com> 2.5-1
- Update to new upstream version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4.1-4
- Build with maven 3.x.
- Use upstream sources.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 2.4.1-2
- Fix review comments.

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 2.4.1-1
- Initial package.
