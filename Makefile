.PHONY: setup start stop backend frontend clean test help

# Default target
all: help

# Colors for terminal output
COLOR_RESET=\033[0m
COLOR_GREEN=\033[32m
COLOR_YELLOW=\033[33m
COLOR_BLUE=\033[34m

# Help command
help:
	@echo "$(COLOR_BLUE)WHOIS Lookup Application - Makefile Commands$(COLOR_RESET)"
	@echo "$(COLOR_YELLOW)make setup$(COLOR_RESET)    - Set up development environment (backend and frontend)"
	@echo "$(COLOR_YELLOW)make start$(COLOR_RESET)    - Start both backend and frontend services"
	@echo "$(COLOR_YELLOW)make backend$(COLOR_RESET)  - Start only the backend service"
	@echo "$(COLOR_YELLOW)make frontend$(COLOR_RESET) - Start only the frontend service"
	@echo "$(COLOR_YELLOW)make stop$(COLOR_RESET)     - Stop all running services"
	@echo "$(COLOR_YELLOW)make clean$(COLOR_RESET)    - Clean up generated files and directories"
	@echo "$(COLOR_YELLOW)make test$(COLOR_RESET)     - Run tests for both backend and frontend"

# Setup both backend and frontend
setup: setup-backend setup-frontend
	@echo "$(COLOR_GREEN)Setup complete for both backend and frontend!$(COLOR_RESET)"

# Setup backend
setup-backend:
	@echo "$(COLOR_BLUE)Setting up backend environment...$(COLOR_RESET)"
	@cd backend && ./setup_venv.sh

# Setup frontend
setup-frontend:
	@echo "$(COLOR_BLUE)Setting up frontend environment...$(COLOR_RESET)"
	@cd frontend && npm install

# Start both services
start:
	@echo "$(COLOR_BLUE)Starting both backend and frontend services...$(COLOR_RESET)"
	@make -j 2 start-both

# Helper target to start both services in parallel
start-both: backend frontend

# Start only backend
backend:
	@echo "$(COLOR_BLUE)Starting backend service...$(COLOR_RESET)"
	@cd backend && ./run.sh

# Start only frontend
frontend:
	@echo "$(COLOR_BLUE)Starting frontend service...$(COLOR_RESET)"
	@cd frontend && npm start

# Stop all services (useful for killing processes)
stop:
	@echo "$(COLOR_BLUE)Stopping all services...$(COLOR_RESET)"
	@-pkill -f "uvicorn main:app" 2>/dev/null || true
	@-pkill -f "react-scripts start" 2>/dev/null || true
	@echo "$(COLOR_GREEN)All services stopped.$(COLOR_RESET)"

# Clean up generated files
clean:
	@echo "$(COLOR_BLUE)Cleaning up...$(COLOR_RESET)"
	@rm -rf backend/__pycache__ backend/app/__pycache__ backend/app/*/__pycache__
	@rm -rf frontend/node_modules frontend/build
	@echo "$(COLOR_GREEN)Cleanup complete.$(COLOR_RESET)"

# Run tests
test: test-backend test-frontend
	@echo "$(COLOR_GREEN)All tests completed.$(COLOR_RESET)"

# Run backend tests
test-backend:
	@echo "$(COLOR_BLUE)Running backend tests...$(COLOR_RESET)"
	@cd backend && source .venv/bin/activate && python -m pytest test_api.py -v

# Run frontend tests
test-frontend:
	@echo "$(COLOR_BLUE)Running frontend tests...$(COLOR_RESET)"
	@cd frontend && npm test
