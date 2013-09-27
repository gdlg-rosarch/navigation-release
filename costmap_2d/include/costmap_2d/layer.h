/*********************************************************************
 *
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2008, 2013, Willow Garage, Inc.
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *
 * Author: David V. Lu!!
 *********************************************************************/
#ifndef COSTMAP_PLUGIN_BASE_H_
#define COSTMAP_PLUGIN_BASE_H_
#include <costmap_2d/costmap_2d.h>
#include <costmap_2d/layered_costmap.h>
#include <string>
#include <tf/tf.h>
#include <tf/transform_listener.h>

namespace costmap_2d
{
class LayeredCostmap;

class Layer
{
public:
  Layer();

  void initialize( LayeredCostmap* parent, std::string name, tf::TransformListener *tf );

  virtual void updateBounds(double origin_x, double origin_y, double origin_yaw, double* min_x, double* min_y,
                             double* max_x, double* max_y) {}
  virtual void updateCosts(Costmap2D& master_grid, int min_i, int min_j, int max_i, int max_j) {}

  virtual void deactivate() {}   // stop publishers
  virtual void activate() {}     // restart publishers if they've been stopped

  virtual void reset() {}

  virtual ~Layer() {}

  bool isCurrent() const
  {
    return current_;
  }

  /** @brief Implement this to make this layer match the size of the parent costmap. */
  virtual void matchSize() {}

  std::string getName() const
  {
    return name_;
  }

  /** @brief Convenience function for layered_costmap_->getFootprint(). */
  const std::vector<geometry_msgs::Point>& getFootprint() const;

  /** @brief LayeredCostmap calls this whenever the footprint there
   * changes (via LayeredCostmap::setFootprint()).  Override to be
   * notified of changes to the robot's footprint. */
  virtual void onFootprintChanged() {}

protected:
  /** @brief This is called at the end of initialize().  Override to
   * implement subclass-specific initialization.
   *
   * tf_, name_, and layered_costmap_ will all be set already when this is called. */
  virtual void onInitialize() {}

  LayeredCostmap* layered_costmap_;
  bool current_;
  bool enabled_; ///< Currently this var is managed by subclasses.  TODO: make this managed by this class and/or container class.
  std::string name_;
  tf::TransformListener* tf_;

private:
  std::vector<geometry_msgs::Point> footprint_spec_;
};

} // namespace costmap_2d
#endif
