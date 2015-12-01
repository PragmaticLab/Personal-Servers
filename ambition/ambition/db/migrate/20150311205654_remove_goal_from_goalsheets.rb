class RemoveGoalFromGoalsheets < ActiveRecord::Migration
  def change
    remove_column :goalsheets, :goals, :text
  end
end
