### ======================================
# Builds
# - MacOS
# - Linux
# - Windows
### =====================================

### =======================================
# Alembic commands
# Usage:
#	make db-revision m="create towns table"
### =======================================
ALEMBIC := poetry run alembic

db_revision:
	$(ALEMBIC) revision --autogenerate -m "$(m)"

db_revision_empty:
	$(ALEMBIC) revision -m "$(m)"

db_upgrade:
	$(ALEMBIC) upgrade head

db_downgrade:
	$(ALEMBIC) downgrade -1

db_current:
	$(ALEMBIC) current

db_history:
	$(ALEMBIC) history

db_heads:
	$(ALEMBIC) heads
