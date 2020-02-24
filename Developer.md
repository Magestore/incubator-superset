# Setup dev environment
- Clone the repository
- Install docker & docker-compose
- Run: docker-compose up -d
- Run: docker-compose exec superset ./docker-init.sh to initialize sample data & permissions
- Access web interface: http://localhost:8088

# Customize frontend (React JS)
- Frontend source location: superset-frontend/src, for example jsx file for Welcome page is located at superset-frontend/src/welcome
- Run npm watch: docker-compose exec superset-node "cd /app/superset-frontend && npm run dev" (for automatically rebuild the source when we make changes)
- Do the customization, wait for node server to rebuild and then reload web to see the result ;)

# Build production docker image
- Clone Amancevice superset repository: https://github.com/amancevice/docker-superset
- Change repository url to our's in Dockerfile
- Run: make (to supervise the build of the new image)
- Run push new image to docker hub and pull to our production server, re-run production superset container and we're done

# Add new jinja_context python function (ex: current_merchant_id)
- define new function to superset/jinja_context.py
- add the new function name to self.context block in def _init_() function

# Flask app routing table
- RUN: docker-compose exec superset flask routes
