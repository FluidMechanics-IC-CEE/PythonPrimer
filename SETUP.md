# GitHub Pages and Solutions Setup

This document explains the repository structure and how the GitHub Pages site and Solutions are organized.

## Repository Structure

```
PythonPrimer/
├── index.md                    # Main page (GitHub Pages homepage)
├── lectures.md                 # Complete lecture overview
├── about.md                    # Course information
├── _config.yml                 # Jekyll configuration
├── Gemfile                     # Ruby dependencies
├── .gitmodules                 # Git submodule configuration
├── Lecture 1/                  # Individual lecture directories
├── Lecture 2/
├── ...
├── Lecture 8/
└── Solutions/ (git submodule)  # Private solutions repository
```

## GitHub Pages Site

### Public Website
- **URL**: https://fluidmechanics-ic-cee.github.io/PythonPrimer/
- **Content**: Course materials, lecture content, exercises (without solutions)
- **Deployment**: Automatic from `main` branch via GitHub Pages

### Configuration
- **Jekyll Theme**: Minima
- **Build Process**: Automatic GitHub Pages Jekyll build
- **Exclusions**: Solutions directory and Python files excluded from public site

## Solutions Management

### Private Repository Setup
The Solutions directory is a **git submodule** pointing to a separate private repository:
- **Repository**: `FluidMechanics-IC-CEE/SolutionsPythonPrimer`
- **Access**: Private repository for instructors only
- **Content**: Complete solutions for all lecture exercises

### Current Solutions Available
- **Lecture 8**: Complete Taylor-Green vortex implementations and best practices examples
- **Lecture 6-7**: Cross-section data file for integration exercises
- **Structure**: Organized by lecture with comprehensive documentation

### Working with Solutions Submodule

#### For Instructors - Accessing Solutions:
```bash
# Clone main repository
git clone https://github.com/FluidMechanics-IC-CEE/PythonPrimer.git
cd PythonPrimer

# Initialize and update solutions submodule
git submodule update --init Solutions

# Solutions are now available in Solutions/ directory
ls Solutions/
```

#### For Instructors - Adding New Solutions:
```bash
# Navigate to solutions submodule
cd Solutions/

# Add new solution files
# Make changes, commit and push to solutions repository
git add .
git commit -m "Add solutions for Lecture X"
git push

# Update main repository to point to new solutions commit
cd ..
git add Solutions
git commit -m "Update solutions submodule"
git push
```

## Privacy and Security

### What's Public (GitHub Pages):
- ✅ Course content and lecture materials
- ✅ Exercise descriptions and starter code
- ✅ Documentation and explanations

### What's Private (Solutions Repository):
- 🔒 Complete solution implementations
- 🔒 Answer keys and worked examples
- 🔒 Instructor guidance and teaching notes

### Jekyll Exclusions
The `_config.yml` file excludes:
- `Solutions/` directory
- All `*.py` files
- Solution-specific patterns

This ensures solutions never appear on the public GitHub Pages site.

## Troubleshooting

### GitHub Pages 404 Errors
1. **Check branch**: GitHub Pages deploys from `main` branch
2. **Verify workflow**: No custom GitHub Actions needed (uses automatic deployment)
3. **Check _config.yml**: Ensure proper Jekyll configuration
4. **Validate structure**: All lecture directories should have README.md files

### Solutions Access Issues
1. **Submodule not initialized**: Run `git submodule update --init Solutions`
2. **Permission denied**: Ensure access to private `SolutionsPythonPrimer` repository
3. **Empty Solutions directory**: Check if submodule is properly configured in `.gitmodules`

### Site Building Issues
1. **Jekyll build errors**: Check Gemfile and _config.yml syntax
2. **Missing content**: Ensure README.md files exist in all lecture directories
3. **Broken links**: Verify URL encoding for directory names with spaces

## Maintenance

### Regular Tasks
- Update solutions in private repository as new exercises are added
- Keep main repository documentation current
- Monitor GitHub Pages deployment status
- Ensure new lecture content follows established structure

### When Adding New Lectures
1. Create lecture directory with README.md
2. Update navigation in index.md and lectures.md
3. Add corresponding solutions directory in private repository
4. Test links and build process

This setup provides a professional course website while maintaining solution privacy.